from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import django, OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'cart', django, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]