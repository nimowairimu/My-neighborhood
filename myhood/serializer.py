from rest_framework import serializers
from .models import Hood, Profile

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        fields = ('name', 'location')


class ViewHoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        fields = ('name', 'location', 'occupants', 'image', 'admin','health_tell', 'police_number')