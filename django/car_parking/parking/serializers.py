from rest_framework import
from .models import CarParking

class CarParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarParking
        fields__all__