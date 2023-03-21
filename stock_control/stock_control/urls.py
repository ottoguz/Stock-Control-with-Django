"""stock_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stock_app.views import home, customers, add_customers, edit_customers, remove_customers, signup, auth_login, auth_logout, products, add_products, edit_products, remove_products, suppliers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup, name="signup"),
    path("", auth_login, name="login"),
    path("logout/", auth_logout, name="logout"),
    path("home/", home, name="home"),
    path("customers/", customers, name="customers"),
    path("add_customers/", add_customers, name="add_customers"),
    path("edit_customer/<int:id>", edit_customers),
    path("remove_customer/<int:id>", remove_customers),
    path("products/", products, name="products"),
    path("add_products/", add_products, name="add_products"),
    path("edit_product/<int:id>", edit_products),
    path("remove_product/<int:id>", remove_products),
    path("suppliers/", suppliers, name="suppliers")
]
