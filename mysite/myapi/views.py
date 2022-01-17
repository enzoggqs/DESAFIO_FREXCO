# views.py
from rest_framework import viewsets

from .serializers import RegionSerializer, FruitSerializer
from .models import Region, Fruit

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('name')
    serializer_class = RegionSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all().order_by('name')
    serializer_class = FruitSerializer