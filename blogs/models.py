from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/images/')
    blog_title = models.CharField(max_length = 100)
    blog_summary = models.CharField(max_length = 1000)
    url = models.URLField(blank=True)
