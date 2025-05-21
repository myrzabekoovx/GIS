# apps/restaurants/filters.py

import django_filters
from .models import Restaurant

class RestaurantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # поиск по части имени
    cuisine_type = django_filters.CharFilter(lookup_expr='iexact')
    rating__gte = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')  # рейтинг от
    rating__lte = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')  # рейтинг до
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine_type', 'rating', 'is_active']
