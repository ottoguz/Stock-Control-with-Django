# Imports for the views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers, Products, Suppliers, Entry_notes
from .forms import CustomerForm, ProductsForm, SuppliersForm, Entry_notesForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#Imports to create send_email()
import smtplib
import email.message


# Function which sends a welcome card to the new user's email when he signs up
def send_email( username, to_email):
    email_body = f"""
                <div style="background-color: #000; height: 260px; width: 500px; border-radius: 5px; display:flex;">
                    <div>
                        <img style=" border-radius: 5px 0px 0px 5px;" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLBTKN85kf359hydWdFGkvXBnrJvmqdGrVbQ&usqp=CAU">
                    </div>
                    <div style="margin:auto;">
                        <p style="color: #fff; text-align: center; font-size: 20px;">Welcome to Stock Control<br><b>{username}</b><br>User Created Successfully</p>
                        <a style="text-align: center; font-size: 20px; margin-left: 38px" href="http://127.0.0.1:8000/">Redirect to Login</a>
                    </div>
                </div> 
                """
    pass_email = "tvmvrnkhkokyrfcz"
    from_email = "softwaretest1987@gmail.com"
    msg = email.message.Message()
    msg["Subject"] = "Welcome to Stock Control"
    msg["From"] = from_email
    msg["To"] = to_email
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_body)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    # Login Credentials for sending the email
    s.login(from_email, pass_email)
    s.sendmail(from_email, to_email, msg.as_string().encode("utf-8"))


# Create your views here.

# View for the home page after login (to be developed)
def home(request):
    if request.user.is_authenticated:
        return render(request, "auth/home.html")
    else:
        messages.error(request, "You must be logged in to grant access to Stock Control")
        return redirect("login")
    

#View for the signup template
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
            send_email(username, email)
            return redirect("login")
    return render(request, "auth/signup.html")

# view for the login template
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
    return render(request, "auth/login.html")


# Logout function
@login_required
def auth_logout(request):
    logout(request)
    messages.info(request, "You have logged out successfully")
    return redirect("login")

# View to show all the customers' data stored in the database
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

# View to create a new customer and include it in the database
def add_customers(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = CustomerForm()
        messages.success(request, f"Customer: {obj.name} added successfully!")
        return redirect("customers")
    return render(request, "customers/add_customers.html", {"form": form})

# View to edit an already existng customer
def edit_customers(request, id=None):
    customer = get_object_or_404(Customers, id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, f"Customer: {obj.name} edited successfully!")
        return redirect("customers")
    return render(request, 'customers/edit_customer.html', {"form": form})

# View to remove a customer
def remove_customers(request, id=None):
    customer = get_object_or_404(Customers, id=id)
    if request.method == "POST":
        messages.success(request, f"Customer: {customer.name} removed successfully!")
        customer.delete()
        return redirect("customers")
    return render(request, "customers/remove_customer.html", {"customer": customer})

# View to show all the products' data stored in the database
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

# View to create a new product and include it in the database
def add_products(request):
    form = ProductsForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ProductsForm()
        messages.success(request, f"Product: {obj.name} successfully created")
        return redirect("products")
    return render(request, "products/add_products.html", {"form": form})

# View to edit an already existng product
def edit_products(request, id=None):
    product = get_object_or_404(Products, id=id)
    form = ProductsForm(request.POST or None, instance=product)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, f"Product: {obj.name} edited successfully!")
        return redirect("products")
    return render(request, "products/edit_product.html", {"form": form})

# View to remove a customer
def remove_products(request, id=None):
    product = get_object_or_404(Products, id=id)
    if request.method == "POST":
        messages.success(request, f"Product: {product.name} removed successfully!")
        product.delete()
        return redirect("products")
    return render(request, "products/remove_product.html", {"product": product})

# View to show all the suppliers' data stored in the database
def suppliers(request):
    suppliers = Suppliers.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        suppliers = Suppliers.objects.filter(
            Q(trading_name__icontains=queryset)|
            Q(company_name__icontains=queryset)|
            Q(cnpj__icontains=queryset)
        )
    paginator = Paginator(suppliers, 5)
    page = request.GET.get('page')
    suppliers = paginator.get_page(page)
    return render(request, "suppliers/suppliers.html", {"suppliers": suppliers})

# View to create a new supplier and include it in the database
def add_suppliers(request):
    form = SuppliersForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = SuppliersForm()
        messages.success(request, f"Company: {obj.company_name} successfully included")
        return redirect("suppliers")
    return render(request, "suppliers/add_suppliers.html", {"form": form})
    
# View to edit an already existng supplier
def edit_supplier(request, id=None):
    supplier = get_object_or_404(Suppliers, id=id)
    form = SuppliersForm(request.POST or None, instance=supplier)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, f"Supplier: {obj.company_name} edited successfully!")
        print()
        return redirect("suppliers")
    return render(request, "suppliers/edit_supplier.html", {"form": form})

# View to remove a supplier
def remove_supplier(request, id=None):
    supplier = get_object_or_404(Suppliers, id=id)
    if request.method == "POST":
        messages.success(request, f"Supplier: {supplier.company_name} removed successfully!")
        supplier.delete()
        return redirect("suppliers")
    return render(request, "suppliers/remove_supplier.html", {"supplier": supplier})

# View to show all the entry notes generated (needs refactoring)
def entry_notes(request):
    entry_notes = Entry_notes.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        customers = Entry_notes.objects.filter(
            Q(supplier__icontains=queryset))
    paginator = Paginator(entry_notes, 5)
    page = request.GET.get('page')
    customers = paginator.get_page(page)
    return render(request, "notes/entry_notes.html", {"entry_notes": entry_notes})

#View to include a new entry note (needs refactoring)
def add_entry_notes(request):
    entries = Entry_notes.objects.all().order_by('-id')
   
    return render(request, "notes/add_entry_notes.html", {"entry": entries})


"""
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
            send_email(username, email)
            return redirect("login")
    return render(request, "auth/signup.html")

"""