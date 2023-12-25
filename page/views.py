from django.shortcuts import render
from django.views import View
from page.models import Product, MeasurementUnit
import json
from django.http import JsonResponse


# Create your views here.
class ProductView(View):
    @staticmethod
    def get(request):
        data_product = Product.objects.all()
        data_measurement_unit = MeasurementUnit.objects.all()

        context = {
            'data_product': data_product,
            'data_measurement_unit': data_measurement_unit
        }
        return render(request, 'page/product.html', context=context)

    # def post(self, request):
    #     # Get the data from the request
    #     global name_sp, size_sp
    #     try:
    #         data_table = json.loads(request.POST.get('data'))
    #         for data in data_table:
    #             name_sp = data['name_sp']
    #             size_sp = data['size_sp']
    #             exists = Product.objects.filter(product_name=name_sp, size=size_sp).exists()
    #             if exists:
    #                 return JsonResponse({"result": "exists",
    #                                      "message": f"Sản phẩm {name_sp} - {size_sp} đã tồn tại trong hệ thống"})
    #             # Save the data in the database
    #             Product.objects.create(product_name=name_sp, size=size_sp)
    #         return JsonResponse({"result": "success",
    #                              "message": f"Sản phẩm {name_sp} - {size_sp} đã được thêm vào hệ thống"})
    #     except Exception as e:
    #         return JsonResponse({"result": "failed"})


def check_product(request):
    if request.method == 'POST':
        print("check_product")
        name_sp = request.POST.get('name_sp')
        size_sp = request.POST.get('size_sp')
        exists = Product.objects.filter(product_name=name_sp, size=size_sp).exists()
        if exists:
            return JsonResponse({"result": "exists",
                                 "message": f"Sản phẩm {name_sp} - {size_sp} đã tồn tại trong hệ thống"})
        return JsonResponse({"result": "success",
                             "message": f"Sản phẩm {name_sp} - {size_sp} có thể thêm vào hệ thống"})
    return JsonResponse({"result": "failed"})
