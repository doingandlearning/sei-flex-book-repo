from django.urls import path
from .views import LocationDetailView, LocationListView


urlpatterns = [
    path("", LocationListView.as_view()),
    path("<int:pk>", LocationDetailView.as_view())
]
