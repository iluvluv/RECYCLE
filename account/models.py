from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)