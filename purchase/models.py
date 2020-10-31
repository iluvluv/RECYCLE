from django.db import models
from account.models import *
from goods.models import *
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    check = models.BooleanField(default=False)
