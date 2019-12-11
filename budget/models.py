from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Loan(models.Model):
    name = models.CharField(max_length=50)
    begin_date = models.DateTimeField('begin date')
    end_date = models.DateTimeField('end date')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class TransactionType(models.Model):
    name = models.CharField(max_length=50)

class BankType(models.Model):
    name = models.CharField(max_length=50)

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    notes = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class BankAccount(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.ForeignKey(BankType, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
