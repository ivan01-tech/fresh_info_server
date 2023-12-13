from django.shortcuts import render
from rest_framework import generics
from .models import Information
from .serializers import InformationSerializers

class InformationList(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializers

class InformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializers
