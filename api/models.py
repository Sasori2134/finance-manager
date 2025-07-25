from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Finance_Manager.functions import get_date

# Create your models here.
class Transaction_data(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE,)
    date = models.DateField(default=get_date)
    category = models.CharField(max_length = 100,)
    itemname = models.CharField(max_length = 200,)
    price = models.DecimalField(max_digits = 10,decimal_places=2)
    transaction_type = models.CharField(max_length=8)
    

class Budget(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    budget = models.DecimalField(max_digits = 10, decimal_places=2,)
    category = models.CharField(max_length=50,)
    date = models.DateField(default=get_date)

class RecurringBills(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.PositiveIntegerField()
    itemname = models.CharField(max_length=14,default='recurring_bill')
    transaction_type = models.CharField(max_length=7,default='expense')