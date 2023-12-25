from django.contrib import admin
from page.models import Product, MeasurementUnit, ImportGoods, ExportGoods 

# Register your models here.

admin.site.register(Product)

admin.site.register(MeasurementUnit)

admin.site.register(ImportGoods)

admin.site.register(ExportGoods)