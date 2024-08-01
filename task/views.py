from django.shortcuts import render
from rest_framework import generics
from .models import ClientAppointment
from .serializers import ClientAppointmentSerializer
from django.http import HttpResponse

# CREATE API view class for client's appointments.

class CreateClientAppointment(generics.CreateAPIView):
    queryset = ClientAppointment.objects.all()
    serializer_class = ClientAppointmentSerializer


def say_hello(request):
    return HttpResponse('Hello World.')

