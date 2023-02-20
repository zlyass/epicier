from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    addresse = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)