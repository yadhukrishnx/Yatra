from . models import *
from rest_framework import serializers



class TouristDestinationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TouristDestination
        fields = '__all__'