from django.urls import path
from .views import *


urlpatterns = [
    path('carousel-get/', CarouselView.as_view(), name='carousel-get')
]