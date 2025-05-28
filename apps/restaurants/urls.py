from django.urls import path, include
from rest_framework import viewsets
from .models import MenuItem

from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

urlpatterns = [
    path('', include(router.urls)),
]