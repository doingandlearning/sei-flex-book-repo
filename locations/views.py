from django.shortcuts import render

from django.shortcuts import render

from rest_framework import generics

from .models import Location
from .serializers import LocationSerializer
# Create your views here.


class LocationListView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
