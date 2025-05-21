from rest_framework import serializers
from .models import Restaurant, MenuItem



class RestaurantSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [ 'id', 'name', 'description', 'location', 'address',
                   'cuisine_type', 'opening_time', 'closing_time',
                   'delivery_radius', 'is_active', 'distance' ]
        read_only_fields = [ 'distance' ]

    def get_distance(self, obj):
        request = self.context.get('request')
        if request and hasattr(request.user, 'current_location'):
            user_location = request.user.current_location
            if user_location and obj.location:
                return user_location.distance(obj.location) * 100  # Convert to meters
        return None


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [ 'id', 'restaurant', 'name', 'description', 'price',
                   'category', 'is_available', 'preparation_time' ]