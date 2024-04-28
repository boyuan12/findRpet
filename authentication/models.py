from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    phone_number = models.CharField(max_length=12)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
