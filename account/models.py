from django.db import models

# Create your models here.

class Account(models.Model):
    type = models.CharField(max_length=30)
    balance = models.FloatField()

