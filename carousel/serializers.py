from .models import Carousel
from rest_framework import serializers

class CaruoselSerializer(serializers.ModelSerializer):
    class Meta():
        model = Carousel
        fields = ['id', 'image', 'position', 'is_active']