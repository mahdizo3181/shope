from rest_framework import serializers
from product.models import Product, Discount


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    discount_id = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all())
    brand = serializers.CharField(max_length=30)
    inventory = serializers.CharField(max_length=40)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.inventory = validated_data.get('inventory', instance.inventory)

    def create(self, validated_data: dict):
        return Product.objects.create(**validated_data)
