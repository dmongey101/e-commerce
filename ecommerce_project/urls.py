"""ecommerce URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from accounts.views import signup, show_profile
from products.views import product_list, show_product
from cart.views import add_to_cart, remove_from_cart, view_cart
from checkout.views import show_checkout
from search.views import do_search
from reviews.views import write_reviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name="home"),
    path('products/<int:id>', show_product, name="product_detail"),
    path('reviews/add/<int:id>', write_reviews, name='write_reviews'),
    path('cart/add/<int:id>', add_to_cart, name='add_to_cart'),
    path('cart/remove/', remove_from_cart, name='remove_from_cart'),
    path('cart/view/', view_cart, name='cart'),
    path('checkout/view/', show_checkout, name='show_checkout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', show_profile, name='profile'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('checkout/pay/', show_checkout, name='pay'),
    path('search', do_search, name='search'),
    
]