from django.db import models

# Create your models here.


class Wallet(models.Model):  
    id = models.IntegerField(primary_key=True)  
    phoneNumber = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2)  
    class Meta:
        db_table = "wallet"  

def __str__(self):
    return self.title