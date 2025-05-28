from rest_framework import viewsets
from django.contrib.gis.db.models.functions import Distance
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        if hasattr(self.request.user, 'location'):
            queryset = queryset.annotate(
                distance=Distance('location', self.request.user.location)
            ).order_by('distance')
        return queryset


class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


