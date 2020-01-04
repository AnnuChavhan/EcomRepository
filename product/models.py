from django.db import models

# Create your models here.
from vendor.models import *

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    category= models.CharField(max_length=100,unique=True)
    quantity=models.IntegerField()
    price =models.FloatField()
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)

