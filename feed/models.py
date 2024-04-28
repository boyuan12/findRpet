from django.db import models

# Create your models here.
class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    pet_type = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

