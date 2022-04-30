from django.db import models

from django.contrib.auth.models import User

from authors.models import Author
from locations.models import Location


class Book(models.Model):
    title = models.CharField(max_length=200)
    year_of_publication = models.IntegerField(
        null=True, blank=True)  # default or null

    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    author = models.ForeignKey(
        Author, null=True, blank=True, on_delete=models.CASCADE, related_name="books")

    locations = models.ManyToManyField(
        Location, blank=True, related_name="books")

    creator = models.ForeignKey(
        User, related_name="books", null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
