from django.db import models

class Carousel(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    position = models.IntegerField(null=True, blank=True, verbose_name='Позиция в карусели')
    is_active = models.BooleanField(default=True, verbose_name='Активное фото')
    
    def __str__(self):
        return f'{self.position}'
    
    class Meta():
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'
