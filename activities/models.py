from django.db import models

# Create your models here.

class Activities(models.Model):
    imagen = models.ImageField(upload_to='imagenes/')
    description = models.TextField(blank=False)
    