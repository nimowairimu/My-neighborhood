from rest_framework import serializers
from .models import NeighbourHood , Profile

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location')


class ViewHoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'occupants', 'image', 'admin','health_tell', 'police_number')