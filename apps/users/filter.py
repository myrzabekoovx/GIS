import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains')
    is_vendor = django_filters.BooleanFilter()
    date_joined_after = django_filters.DateTimeFilter(field_name='date_joined', lookup_expr='gte')

    class Meta:
        model = User
        fields = ['email', 'is_vendor', 'date_joined_after']