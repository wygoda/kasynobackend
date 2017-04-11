from django.db import models
from decimal import *

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    balance = models.Decimal(max_digits=13, decimal_places=2) #liczba wszystkich cyfr, cyfry po przecinku (dokladnosc)

    def modifyBalance(amount):
        try:
            balance += Decimal(amount)
            return 0
        except Exception as e:
            print(e)
            return 1

    def authenticate(password):
        return True if self.password==password else False
