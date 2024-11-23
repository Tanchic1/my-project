from django.shortcuts import render
from .models import Product

# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products':products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product':product})

def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/create_order.html', {'product':product})