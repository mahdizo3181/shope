from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from order.models import Order, OrderItem
from .models import Product, Category
import json


def home(request, slug=None):
    product = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        product = product.filter(category=category)
    return render(request, 'product/product.html', {'product': product, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {'product': product})


def updateItem(request):
    data = json.loads(request.body)
    user = data['user']
    if user == 'AnonymousUser':
        messages.success(request, '.برای ثبت سفارش ابتدا باید وارد اکانتت خود شوید', 'warning')
    else:
        customer = request.user
        print(customer)
        productID = data['productID']
        # action = data['action']
        product = Product.objects.get(id=productID)

        # order, created = Order.objects.get_or_create(customer_id=customer)
        order = Order.objects.create(customer_id=customer)

        OrderItem.objects.get_or_create(order_id=order, product=product, customer_id=customer)
    return JsonResponse('Item was added', safe=False)
