from django.db import models
from django.urls import reverse

# Create your models here.
class Hoya(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    scent = models.CharField(max_length=100)
    img = models.URLField(max_length=200)

    # new code below
    def __str__(self):
        return self.name
      # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hoya_id': self.id})