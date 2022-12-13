from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class HelloModel(models.Model):
    name= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    