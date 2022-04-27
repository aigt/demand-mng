from .models import Demand
from rest_framework import viewsets, permissions
from .serializers import DemandSerializer

class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DemandSerializer
