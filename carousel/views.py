import requests
from django.shortcuts import render
from .serializers import CaruoselSerializer
from .models import Carousel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CarouselView(APIView):
    serializer_class = CaruoselSerializer

    def get(self, request, *args, **kwargs):
        
        active_carousels = Carousel.objects.filter(is_active=True)
        serializer = CaruoselSerializer(active_carousels, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

