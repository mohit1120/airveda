from rest_framework import serializers
#from rest_framework import device
from .models import device,temperature, humidity
class deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields=('uid','name')
        #fields = '__all__'


class temperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = '__all__'


class humiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = humidity
        fields = '__all__'


