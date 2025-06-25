from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    assigned_market = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Market(models.Model):
    market_name = models.CharField(max_length=50, unique=True)
    number_of_traders_registered = models.IntegerField(default=0)
    collection_day = models.CharField(max_length=50)
    assigned_agent = models.CharField(max_length=50)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.market_name

class Trader(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    market_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    date_enrolled = models.DateField()
    market = models.ForeignKey(Market, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class FabricCatalogue(models.Model):
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    last_update_date = models.DateField()
    fabric_type = models.CharField(max_length=50)
    fabric_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fabric_type

class ClothesListing(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('pickup_schedules', 'Pickup Schedules'),
        ('pickup_completed', 'Pickup Completed'),
    ]
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    estimated_weight = models.DecimalField(max_digits=10, decimal_places=2)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    fabric = models.ForeignKey(FabricCatalogue, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)




