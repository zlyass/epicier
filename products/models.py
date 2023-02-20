from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    selling_price=models.FloatField()
    price=models.FloatField()
