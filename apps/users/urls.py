from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomTokenObtainPairView
from django.urls import include, path


router = DefaultRouter()
router.register(r'users', UserViewSet)


# def include(urls):
    #pass

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]