# apps/order/views.py

from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from .filters import OrderFilter
from django_filters.rest_framework import DjangoFilterBackend

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
