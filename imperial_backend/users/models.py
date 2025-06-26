from django.db import models

# Create your models here.

class Trader(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    market_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date_enrolled = models.DateField()

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    assigned_market = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class RecyclingCompany(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    licence_number = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name
