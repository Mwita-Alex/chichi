from django.db import models

# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='events/images/')
    event_title = models.CharField(max_length = 100)
    event_date_added = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    event_summary = models.CharField(max_length = 1000)
    url = models.URLField(blank=True)


    def __str__(self):
        return self.event_title
