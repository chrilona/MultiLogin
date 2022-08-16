from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_supplier = models.BooleanField
    is_employee = models.BooleanField
    first_name = models.CharField(max_length=80,null=True)
    last_name = models.CharField(max_length=80,null=True)

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="is_supplier")
    phone_number = models.CharField(max_length=10,null=True)
    product_name = models.CharField(max_length=100,null=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="is_employee")
    phone_number = models.CharField(max_length=10,null=True)
    department = models.CharField(max_length=30,null=True)    
# Create your models here.
