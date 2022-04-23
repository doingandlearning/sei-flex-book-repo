from rest_framework import serializers
from authors.models import Author

from books.models import Book
from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("name", )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first_name",)


class BookSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ("id", "title", "year_of_publication",
                  "rating", "locations", "author")

    def create(self, data):
        author_data = data.pop("author")
        location_data = data.pop("locations")

        book = Book(**data)

        if author_data:
            author, _created = Author.objects.get_or_create(**author_data)
            book.author = author

        # Need to save to get the id
        book.save()

        if location_data:
            for location in location_data:
                newLocation, _created = Location.objects.get_or_create(
                    **location)
                book.locations.add(newLocation)

        # render to the api
        return book

    def update(self, book, data):
        author_data = data.pop("author")
        location_data = data.pop("locations")

        book.title = data.get("title", book.title)
        book.rating = data.get("rating", book.rating)
        book.year_of_publication = data.get(
            "year_of_publication", book.year_of_publication)

        if author_data:
            author, _created = Author.objects.get_or_create(**author_data)
            book.author = author

        if location_data:
            for location in location_data:
                newLocation, _created = Location.objects.get_or_create(
                    **location)
                book.locations.add(newLocation)

        # save to the database
        book.save()

        # render to the api
        return book
