from django.contrib import admin
from .models import OffCode, Order, OrderItem


# Register your models here.

@admin.register(OffCode)
class OffCodeAdmin(admin.ModelAdmin):
    fields = ['code', 'value', 'type', 'max_price']
    list_display = ['value', 'type', 'max_price']
    search_fields = ['type']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['customer_id', 'address', 'off_code', ]
    list_display = ['customer_id', 'address', 'off_code', ]
    search_fields = ['customer_id']


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    fields = ['order_id', 'product', 'quantity']
    list_display = ['quantity', "product", 'order_id']
    search_fields = ['product']
