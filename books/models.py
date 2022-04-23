from django.db import models

from django.contrib.auth.models import User

from authors.models import Author
from locations.models import Location
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    year_of_publication = models.IntegerField(
        null=True, blank=True)  # default or null

    rating = models.IntegerField()

    author = models.ForeignKey(
        Author, null=True, blank=True, on_delete=models.CASCADE, related_name="books")

    locations = models.ManyToManyField(
        Location, blank=True, related_name="books_set_here")

    creator = models.ForeignKey(
        User, related_name="books", null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
