from django import forms
from .models import Customers, Products




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ["name", "email", "phone", "cpf"]
        widgets = {
            "name":forms.TextInput(attrs={"placeholder":"Inform customer name"}),
            "email":forms.TextInput(attrs={"placeholder":"Inform customer email"}),
            "phone":forms.TextInput(attrs={"placeholder":"Inform customer phone"}),
            "cpf":forms.TextInput(attrs={"placeholder":"Inform customer cpf", "id":"cpf"})
        }

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["status", "name", "category"]
        
        
    