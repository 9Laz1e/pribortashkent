from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Вложенный сериализатор для отображения объекта категории

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'image', 'description', 'cost']


