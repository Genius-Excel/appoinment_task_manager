from django.shortcuts import render
from rest_framework import generics
from .models import ClientAppointment
from .serializers import ClientAppointmentSerializer


# CREATE API view class for client's appointments.

class CreateClientAppointment(generics.CreateAPIView):
    queryset = ClientAppointment.objects.all()
    serializer_class = ClientAppointmentSerializer



