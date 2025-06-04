from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True)  # Статус изменяется отдельно

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'status', 'total_price', 'created_at', 'delivery_address', 'contact_phone']
        read_only_fields = ['user', 'total_price']

class CreateOrderSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.DictField(
            child_fields={
                'product_name': serializers.CharField(max_length=100),
                'price': serializers.DecimalField(max_digits=6, decimal_places=2),
                'quantity': serializers.IntegerField(min_value=1)
            }
        )
    )
    delivery_address = serializers.CharField(max_length=200)
    contact_phone = serializers.CharField(max_length=20)