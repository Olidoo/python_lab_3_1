from rest_framework import serializers
from .models import CO2Sensors


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CO2Sensors
        fields = "__all__"


class SensorMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CO2Sensors
        fields = ('name', 'measurement_date', 'measurement_time', 'temperature')