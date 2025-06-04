from rest_framework import serializers
from .models import Restaurant, MenuItem, Order, OrderItem


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    item = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [ 'item', 'quantity' ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [ 'id', 'user', 'items', 'status', 'total_price', 'created_at' ]
