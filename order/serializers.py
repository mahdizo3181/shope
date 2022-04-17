from rest_framework import serializers
from .models import *


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order_id', 'product', 'quantity']
