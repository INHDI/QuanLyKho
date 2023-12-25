from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('product/check_product/', views.check_product, name='check_product'),
]