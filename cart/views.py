from django.shortcuts import get_object_or_404, render, redirect
from products.models import Product

# Create your views here.
def add_to_cart(request, id):
    product = str(id)
    quantity =  int(request.POST["quantity"])
    
    cart = request.session.get('cart', {})
    cart[product] = cart.get(product, 0) + quantity 
    request.session['cart'] = cart
    
    return redirect("/")
    
def remove_from_cart(request):
    product_id = request.POST['product']

    cart = request.session.get('cart', {})
    del cart[product_id]

    request.session['cart'] = cart

    return redirect("/cart/view/")    
   
   
    
def view_cart(request):
    cart = request.session.get('cart', {})
    
    cart_items = []
    cart_total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': item_total
        })
        cart_total += item_total

    return render(request, "cart/view_cart.html", {'cart_items': cart_items, 'cart_total': cart_total})