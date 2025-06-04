from .filters import OrderFilter

class OrderViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
