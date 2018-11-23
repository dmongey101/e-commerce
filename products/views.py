from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from reviews.forms import ReviewsForm
from reviews.models import Reviews

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products" : products})
    
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ReviewsForm()
    return render(request, "products/product_details.html", {"product" : product, "form": form})
