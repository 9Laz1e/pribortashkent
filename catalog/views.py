from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CategoryView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, context={'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, product_id=None, *args, **kwargs):
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                serializer = ProductSerializer(product, context={'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Если course_id не указан, возвращаем полный список курсов
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
            
    



class ProductsByCategoryView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, category_id, *args, **kwargs):
        # Проверяем, существует ли категория
        category = get_object_or_404(Category, id=category_id)
        # Получаем все товары для указанной категории
        products = Product.objects.filter(category=category)
        # Сериализуем данные
        serializer = ProductSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)