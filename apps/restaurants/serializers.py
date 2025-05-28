from rest_framework import serializers
from .models import Restaurant, MenuItem


class RestaurantSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [ 'id', 'name', 'address', 'location', 'distance' ]

    def get_distance(self, obj):
        request = self.context.get('request')
        if request and hasattr(request.user, 'location'):
            return request.user.location.distance(obj.location) * 100  # в метрах
        return None


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [ 'id', 'name', 'price' ]