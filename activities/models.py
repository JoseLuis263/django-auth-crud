from django.db import models

# Create your models here.

class Activities(models.Model):
    #image = models.ImageField(null=True, blank=True, upload_to='image/')
    #video_link = models.URLField(blank=True, max_length=200)
    description = models.TextField(blank=False)
    
    