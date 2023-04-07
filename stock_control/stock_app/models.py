from django.db import models


# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=250, null=False)
    email = models.EmailField(default="")
    phone = models.CharField(max_length=15, null=False)
    cpf = models.CharField(max_length=14, unique=True, null=False)
    creation_date = models.DateField(auto_now_add=True)
    
class Products(models.Model):
    class Categories(models.TextChoices):
        CELL_PHONES = "Cell Phones"
        APPLIANCES = "Appliances"
        COMP_PARTS = "Computer Parts"
        FURNITURE = "Furniture"

    status = models.BooleanField(default=False, verbose_name=f"Status: Out of Stock / Available")
    name = models.CharField(max_length=250, null=False)
    category = models.CharField(max_length=50, choices=Categories.choices)
    creation_date = models.DateField(auto_now_add=True)

class Suppliers(models.Model):
    status = models.BooleanField(default=False, verbose_name=f"Status: Inactive / Active")
    trading_name = models.CharField(max_length=250, null=False)
    company_name = models.CharField(max_length=250, null=False)
    cnpj = models.CharField(max_length=18, unique=True, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(default="")

class Entry_notes(models.Model):
    class Choices(models.TextChoices):
    
        CHOICES = Suppliers.objects.filter().values("company_name")
    supplier = models.CharField(max_length=500, choices=Choices.choices)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField(default=0.0)
