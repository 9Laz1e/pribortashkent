from django.contrib import admin
from .models import Carousel

class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'position', 'is_active']
    list_display_links = ['image']
    list_editable = ['position', 'is_active']




admin.site.register(Carousel, CarouselAdmin)