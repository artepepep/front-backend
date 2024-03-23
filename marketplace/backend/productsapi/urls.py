from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/add-product/', CreateProductAPI.as_view(), name='create-product'),
    path('api/v1/products-all/', GetAllProductsAPI.as_view(), name='get-all-products'),
    path('api/v1/products/<int:quantity>/', GetFixAmountProductsAPI.as_view(), name='fix-latest-products'),
    path('api/v1/products-detail/<int:pk>/', ProductDetailAPI.as_view(), name='delete-product'),
    path('api/v1/products/<str:keyword>/', ProductSearchAPI.as_view(), name='search-by-keyword'),
    path('api/v1/basket/', GetBasketAPI.as_view(), name='get-basket'),
    path('api/v1/basket/<int:pk>/', PutBasketAPI.as_view(), name='put-basket'),
    path('api/v1/categorys/', CategoryAPI.as_view(), name='get-categorys'),
]