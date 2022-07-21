from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
CARES = (
    ('W', 'Watering'),
    ('S', 'Sun light'),
    ('N', 'Nutrition')
)

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

class Cultivation(models.Model):
    date = models.DateField("Caring Date")
    care = models.CharField(max_length=1,
    choices=CARES, 
    default=CARES[0][0])
    # create a hoya_id FK
    hoya = models.ForeignKey(Hoya, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
      return f"{self.get_care_display()} on {self.date}"
    
     # change the default sort
    class Meta:
      ordering = ['-date']
