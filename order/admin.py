from django.contrib import admin
from .models import OffCode, Order, OrderItem


# Register your models here.

@admin.register(OffCode)
class OffCodeAdmin(admin.ModelAdmin):
    fields = ['code', 'value', 'type', 'max_price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['customer_id', 'amount', ]


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    fields = ['order_id', 'product', 'quantity']
