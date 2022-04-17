from django.contrib import admin
from .models import Category, Product, Discount


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'category_id', 'is_sub', 'slug']
    list_display = ['name', 'category_id', 'is_sub', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    fields = ['name', 'price', 'category', 'slug', 'discount_id', 'brand', 'inventory', 'image', 'description',
              'available', ]
    list_display = ['name', 'price', 'discount_id', 'brand', 'inventory', 'image',
                    'available', ]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    fields = ['value', 'type', 'max_price']
    list_display = ['value', 'type', 'max_price']
    search_fields = ['type']
