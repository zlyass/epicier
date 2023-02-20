from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=50)
    password =models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)