from django.shortcuts import render
from products.models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {"products" : products})
