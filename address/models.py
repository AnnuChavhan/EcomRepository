from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=100,unique=True)
    state= models.CharField(max_length=100,unique=True)
    pincode=models.IntegerField()
