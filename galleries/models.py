from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/images/')
    image_title = models.CharField(max_length = 500)



