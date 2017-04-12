from django.db import models
from decimal import *

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=13, decimal_places=2) #liczba wszystkich cyfr, cyfry po przecinku (dokladnosc)

    def modifyBalance(self, amount):
        try:
            self.balance += Decimal(amount)
            return True
        except Exception as e:
            print(e)
            return False

    def authenticate(self, password):
        return True if self.password==password else False

    def __str__(self):
        result = str(self.id) + ", " + self.username + ", " + str(self.balance)
        return result
