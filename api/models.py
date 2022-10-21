from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


import string
import random



def generate_invoice_token():
    
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',k=10))
   

class Invoice(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    invoice_items_count = models.IntegerField()
    recipient_name = models.CharField(max_length=50,blank=False,null=False)
    description = models.CharField(max_length=300)
    reference_code = models.CharField(max_length=10,unique=True,default=generate_invoice_token)


    
