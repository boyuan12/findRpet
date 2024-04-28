from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=256, default="N/A")
    pet_description = models.TextField()
    pet_picture = models.URLField()
    status = models.BooleanField()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

