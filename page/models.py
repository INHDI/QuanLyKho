from django.db import models


# Đơn vị tính
class MeasurementUnit(models.Model):
    text = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.text


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=False)
    size = models.CharField(max_length=200, blank=True, null=True)
    c_time = models.DateTimeField(auto_now_add=True)
    dvt = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name + " - " + self.size if self.size is not None else self.product_name


# Nhập hàng
class ImportGoods(models.Model):
    product_import = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    import_source = models.CharField(max_length=200, null=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_import.product_name + " - " + self.product_import.size


# Xuất hàng
class ExportGoods(models.Model):
    product_export = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    output_source = models.CharField(max_length=200, null=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_export.product_name + " - " + self.product_export.size
