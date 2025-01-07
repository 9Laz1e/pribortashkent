from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Наименование Категории')

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', verbose_name='Категория товара')
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Название товара')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение товара')
    description = HTMLField(null=True, blank=True, verbose_name='Описание товара')
    cost = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='Цена товара')

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'