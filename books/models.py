from django.db import models

from django.contrib.auth.models import User

from authors.models import Author
from locations.models import Location
from users.models import BooksUser

GENRES = [
    ('Not classified', "This book can't be classified as a particular genre"),
    ('Action', 'Action and adventure books constantly have you on the edge of your seat with excitement'),
    ('Classics', 'You may think of these books as the throwback readings you were assigned in English class. '),
    ('Comic', "The stories in comic books and graphic novels are presented to the reader through engaging, sequential narrative art (illustrations and typography) that's either presented in a specific design or the traditional panel layout you find in comics."),
    ('Detective', 'The plot always revolves around a crime of sorts that must be solved—or foiled—by the protagonists.'),
]

LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
    ('cn', 'Chinese'),
    ('es', 'Spanish')
]


class Book(models.Model):
    title = models.CharField(max_length=200)
    year_of_publication = models.IntegerField(
        null=True, blank=True)  # default or null

    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default='en'
    )

    genre = models.CharField(
        max_length=500,
        choices=GENRES,
        default='Action',
    )

    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    author = models.ForeignKey(
        Author, null=True, blank=True, on_delete=models.CASCADE, related_name="books")

    locations = models.ManyToManyField(
        Location, blank=True, related_name="books")

    creator = models.ForeignKey(
        BooksUser, related_name="books", null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
