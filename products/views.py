from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {"products" : products})
    
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_details.html", {"product" : product})
