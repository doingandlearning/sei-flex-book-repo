from django.shortcuts import render

from rest_framework import generics

from .models import Author
from .serializers import AuthorSerializer
# Create your views here.


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
