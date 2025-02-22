from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']




class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'image', 'description', 'cost']
    list_display_links = ['name']
    search_fields = ['name']
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)