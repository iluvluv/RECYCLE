from django.db import models
from account.models import *
# Create your models here.

class Goods(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    money = models.IntegerField()
    kinds = models.CharField(max_length=30)

    def __str__(self):
        return self.title