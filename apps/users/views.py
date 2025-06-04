from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    http_method_names = ['get', 'post', 'patch']  # Запрещаем DELETE

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)