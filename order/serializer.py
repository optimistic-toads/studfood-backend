from rest_framework import serializers
from .models import Order, User
from products.models import Product
from products.serializer import ProductsListSerializer


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class OrderPostSerializer(serializers.Serializer):
    product = ProductSerializer(many=True)

    def create(self, validated_data):
        product = validated_data.pop('product', [])
        order = Order.objects.create(**validated_data)

        for product_data in product:
            prod = Product.objects.get(pk=product_data.get('id'))
            order.product.add(prod)
        return order


class OrderGetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product = ProductsListSerializer(many=True)
    created_date = serializers.DateTimeField()

    def create(self, validated_data):
        product = validated_data.pop('product', [])
        order = Order.objects.create(**validated_data)

        for product_data in product:
            prod = Product.objects.get(pk=product_data.get('id'))
            order.product.add(prod)
        return order
