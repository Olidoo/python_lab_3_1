from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *


def index(request):
    sensors = CO2Sensors.objects.all()
    return render(request, 'index.html', {'sensors': sensors})


def sensor_page(request, id):
    try:
        sensor = CO2Sensors.objects.get(id=id)
        sensor = [(str(k).capitalize().replace('_', ' '), v) for k, v in sensor.__dict__.items()]
    except ObjectDoesNotExist:
        return HttpResponse("Sorry, wrong id")
    return render(request, 'sensor_info.html', {'server': sensor[1:]})


# @login_required(login_url=settings.LOGIN_URL)
def secure(request):
    return render(request, 'secure.html')


class SensorsAPIView(APIView):
    def get(self, request):
        queryset = CO2Sensors.objects.all()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            queryset = CO2Sensors.objects.get(id=id)
            serializer = SensorSerializer(queryset)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class SensorMeasurementAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            queryset = CO2Sensors.objects.get(id=id)
            serializer = SensorMeasurementSerializer(queryset)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class FilesAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        file = request.FILES['csv']
        file_name = default_storage.save(file.name, file)
        response = {
            file_name: 'saved'
        }

