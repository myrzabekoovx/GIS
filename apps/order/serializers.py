from rest_framework import serializers
from .models import Cart, CartItem, Order, OrderItem
from apps.restaurants.serializers import MenuItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    total_item_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [ 'id', 'menu_item', 'quantity', 'price', 'total_item_price' ]

    def get_total_item_price(self, obj):
        return obj.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [ 'id', 'user', 'items', 'total_price', 'created_at', 'updated_at' ]

    def get_total_price(self, obj):
        return obj.total_price


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = [ 'id', 'menu_item', 'quantity', 'price' ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = [ 'id', 'user', 'restaurant', 'status', 'status_display',
                   'created_at', 'updated_at', 'delivery_address',
                   'total_price', 'notes', 'items' ]
        read_only_fields = [ 'user', 'restaurant', 'total_price', 'created_at', 'updated_at' ]