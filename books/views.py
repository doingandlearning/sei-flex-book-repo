from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.permissions import IsAuthor, IsAuthorOrReadOnly, IsPutOrGetMethod, IsSafeMethod
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSafeMethod | IsAuthor]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
