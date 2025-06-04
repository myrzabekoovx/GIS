import django_filters
from .models import Order
from django.db import models

class OrderFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    min_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['status', 'created_after', 'created_before', 'min_price', 'max_price']