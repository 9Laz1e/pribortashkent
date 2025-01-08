from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer()  # Вложенный сериализатор для отображения объекта категории

    class Meta:
        model = Product
        fields = ['id', 'category_name', 'name', 'image', 'description', 'cost']


