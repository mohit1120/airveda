# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import device, temperature, humidity
from .serializers import deviceSerializer, temperatureSerializer, humiditySerializer




class deviceAdd(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = deviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

class deviceList(APIView):
    def get(self, request):
        print(request.method)
        devices = device.objects.all()
        serializer = deviceSerializer(devices, many=True)
        print(serializer.data[0])
        return Response(serializer.data)
        
   


class deviceOne(APIView):
    def get(self, request, id):
        print(id)
        devices = device.objects.filter(uid=id)
        print(devices)
        serializer = deviceSerializer(devices, many=True)
        return Response(serializer.data)
   
    
class deviceRemove(APIView):
    def get(self, request, id):
        print(id)
        devices = device.objects.filter(uid=id)
        print(devices)
        devices.delete()
        return HttpResponse('Data deleted successfully')



class temperatureList(APIView):
    def get(self, request, id):
        startDate = request.query_params['startDate']
        endDate = request.query_params['endDate']
        devices = device.objects.filter(uid=id)
        temperatures = temperature.objects.filter(Date__gte=startDate, Date__lte=endDate, uid=id)
        #temperatures = temperature.objects.filter(uid=id)
        if len(devices) != 0:
            devices = deviceSerializer(devices, many=True)
            print(devices.data)
            if len(temperatures) != 0:
                temperatures = temperatureSerializer(temperatures, many=True)
                return Response(temperatures.data)
            else:
                return HttpResponse("No Temperature Recorded")    
        else:
            return HttpResponse("No Device Found with this Entered Id")   

class temperatureAdd(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = temperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class humidityList(APIView):
    def get(self, request, id):
        startDate = request.query_params['startDate']
        endDate = request.query_params['endDate']
        devices = device.objects.filter(uid=id)
        humiditydata = humidity.objects.filter(Date__gte=startDate, Date__lte=endDate, uid=id)
        if len(devices) != 0:
            devices = deviceSerializer(devices, many=True)
            print(devices.data)
            if len(humiditydata) != 0:
                humiditydata = humiditySerializer(humiditydata, many=True)
                return Response(humiditydata.data)
            else:
                return HttpResponse("No Humidity Recorded")    
        else:
            return HttpResponse("No Device Found with this Entered Id")   

class humidityAdd(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = humiditySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)