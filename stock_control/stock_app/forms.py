from django import forms
from .models import Customers, Products, Suppliers, Entry_notes


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
        
        
class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ["status", "trading_name", "company_name", "cnpj", "phone", "email"]
        widgets = {
            "trading_name":forms.TextInput(attrs={"placeholder":"Inform trading name"}),
            "company_name":forms.TextInput(attrs={"placeholder":"Inform company name"}),
            "cnpj":forms.TextInput(attrs={"placeholder":"Inform company cnpj"}),
            "phone":forms.TextInput(attrs={"placeholder":"Inform comapny phone"}),
            "email":forms.TextInput(attrs={"placeholder":"Inform company email address"})
        }

class Entry_notesForm(forms.ModelForm):
    class Meta:
        model = Entry_notes
        fields = ["supplier", "date_time", "value"]
    

    