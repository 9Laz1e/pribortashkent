from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, context={'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, context={'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)