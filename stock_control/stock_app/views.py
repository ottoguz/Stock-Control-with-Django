from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers, Products
from .forms import CustomerForm, ProductsForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        messages.error(request, "You must be logged in to grant access to Stock Control")
        return redirect("login")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpass = request.POST.get("confpass")
        if password != confpass:
            messages.error(request, "Your password and confirmation do not match")
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            my_user.clean_fields()
            messages.success(request, f"User: {my_user.username} successfully created")
            return redirect("login")
    return render(request, "signup.html")

def auth_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome to Stock Control: {username}")
            return redirect("home")
        else:
            messages.error(request, "Username or password incorrect")
    return render(request, "login.html")

@login_required
def auth_logout(request):
    logout(request)
    messages.info(request, "You have logged out successfully")
    return redirect("login")

def customers(request):
    customers = Customers.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        customers = Customers.objects.filter(
            Q(name__icontains=queryset)|
            Q(email__icontains=queryset)|
            Q(phone__icontains=queryset)|
            Q(cpf__icontains=queryset)
        )
    paginator = Paginator(customers, 5)
    page = request.GET.get('page')
    customers = paginator.get_page(page)
    return render(request, "customers/customers.html", {"customers": customers})


def add_customers(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = CustomerForm()
        messages.success(request, f"Customer: {obj.name} added successfully!")
        return redirect("customers")
    return render(request, "customers/add_customers.html", {"form": form})


def edit_customers(request, id=None):
    customer = get_object_or_404(Customers, id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, f"Customer: {obj.name} edited successfully!")
        return redirect("customers")
    return render(request, 'customers/edit_customer.html', {"form": form})


def remove_customers(request, id=None):
    customer = get_object_or_404(Customers, id=id)
    if request.method == "POST":
        messages.success(request, f"Customer: {customer.name} removed successfully!")
        customer.delete()
        return redirect("customers")
    return render(request, "customers/remove_customer.html", {"customer": customer})

def products(request):
    products = Products.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        products = Products.objects.filter(
            Q(status__icontains=queryset)|
            Q(name__icontains=queryset)|
            Q(category__icontains=queryset)
        )
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products/products.html", {"products": products})

def add_products(request):
    form = ProductsForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ProductsForm()
        messages.success(request, f"Product: {obj.name} successfully created")
        return redirect("products")
    return render(request, "products/add_products.html", {"form": form})


       
        

