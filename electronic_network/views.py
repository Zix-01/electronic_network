from rest_framework import viewsets
from .models import Factory, RetailNetwork, Entrepreneur
from .serializers import FactorySerializer, RetailNetworkSerializer, EntrepreneurSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['contact_info__country']
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['contact_info__country']
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['contact_info__country']
    search_fields = ['name']
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Запрещение обновления outstanding_debt через API
        serializer.save(outstanding_debt=self.get_object().outstanding_debt)
