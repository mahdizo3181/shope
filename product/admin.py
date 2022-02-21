from django.contrib import admin
from .models import Category, Product, Discount


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'category_id', 'is_sub']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    fields = ['name', 'price', 'category', 'discount_id', 'brand', 'inventory', 'image', 'description', 'available']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    fields = ['value', 'type', 'max_price']
