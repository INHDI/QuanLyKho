from django.shortcuts import render
from django.views import View

from page.models import Product
import json
from django.http import JsonResponse


# Create your views here.
class ProductView(View):
    def get(self, request: object) -> object:
        data_product = Product.objects.all()
        context = {
            'data_product': data_product
        }
        return render(request, 'page/product.html', context=context)

    # Save data from the axjx request
    def post(self, request):
        # Get the data from the request
        try:
            data_table = json.loads(request.POST.get('data'))
            for data in data_table:
                name_sp = data['name_sp']
                size_sp = data['size_sp']
                exists = Product.objects.filter(product_name=name_sp, size=size_sp).exists()
                if exists:
                    return JsonResponse({"result": "exists",
                                         "message": f"Sản phẩm {name_sp} - {size_sp} đã tồn tại trong hệ thống"})
                # Save the data in the database
                Product.objects.create(product_name=name_sp, size=size_sp)
            return JsonResponse({"result": "success",
                                 "message": f"Sản phẩm {name_sp} - {size_sp} đã được thêm vào hệ thống"})
        except Exception as e:
            return JsonResponse({"result": "failed"})
