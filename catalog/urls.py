from django.urls import path
from .views import *


urlpatterns = [
    path('categories-get/', CategoryView.as_view(), name='categories-get'),
    path('products-get/', ProductView.as_view(), name='products-get')
]