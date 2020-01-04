from django.db import models

# Create your models here.
from address.models import *
from account.models import *

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100,unique=True)
    age=models.IntegerField()
    account=models.OneToOneField(Account,on_delete=models.CASCADE,null=True)
    address=models.ManyToManyField(Address)
#Customer(id=0,name='',email='',age=0)