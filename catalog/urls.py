from django.urls import path
from .views import *


urlpatterns = [
    path('categories-get/', CategoryView.as_view(), name='categories-get'),
    path('products/category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products-get-by-category'),
    path('products-get/', ProductView.as_view(), name='products-get')
]