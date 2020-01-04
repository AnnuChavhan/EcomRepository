from django.db import models

# Create your models here.
from address.models import *
from account.models import *

class Vendor(models.Model):
    name = models.CharField(max_length=100,unique=True)
    remarks=models.IntegerField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    account = models.OneToOneField(Account,on_delete=models.CASCADE,null=True)
