# apps/restaurants/views.py

from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from .filters import RestaurantFilter
from django_filters.rest_framework import DjangoFilterBackend

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestaurantFilter



