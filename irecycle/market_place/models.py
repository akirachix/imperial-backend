from django.db import models

# Create your models here
class RecyclingCompany(models.Model):
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    licence_number = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

class Collection(models.Model):
    collection_day = models.CharField(max_length=50)
    collection_point = models.CharField(max_length=50)
    market = models.ForeignKey(Market, on_delete=models.SET_NULL, null=True)
    actual_weight_kgs = models.DecimalField(max_digits=10, decimal_places=2)
    collection_date = models.DateField()
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    fabric = models.ForeignKey(FabricCatalogue, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collection {self.id} on {self.collection_date}"

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('initiated', 'Initiated'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    fabric_catalogue = models.ForeignKey(FabricCatalogue, on_delete=models.CASCADE)
    company = models.ForeignKey(RecyclingCompany, on_delete=models.CASCADE)

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    collection = models.OneToOneField(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.id} - {self.payment_status}"

