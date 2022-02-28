from django.shortcuts import render, get_object_or_404
from .models import Product, Category


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
