from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)


class EmailConfirm(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    key = models.CharField(max_length=30)
    is_confirmed = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)

