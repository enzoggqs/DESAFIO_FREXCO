# serializers.py
from rest_framework import serializers

from .models import Region, Fruit

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('name',)

class FruitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fruit
        fields = ('name', 'region')