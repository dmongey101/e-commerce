from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def show_checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100), 
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect("/")
            else:
                messages.error(request, "Unable to take payment")
        else: 
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:

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
    
    
        order_form = OrderForm()
        payment_form = MakePaymentForm()
    
        return render(request, "checkout/checkout.html", {'cart_items': cart_items, 'cart_total': cart_total, "order_form" : order_form, "payment_form" : payment_form, "publishable" : settings.STRIPE_PUBLISHABLE})