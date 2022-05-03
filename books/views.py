from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.permissions import IsAuthor, IsAuthorAndPremiumUser, IsAuthorOrReadOnly, IsPremiumUser, IsPutOrGetMethod, IsSafeMethod
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    # Permission classes are not applied for list views -> only for views
    # which deal with a single instance of an object.
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Combination of different permission classes to restrict actions on a particular book
    permission_classes = [IsAuthorAndPremiumUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
