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
        fields = ("title", "year_of_publication",
                  "rating", "locations", "author")

    def create(self, data):
        author_data = data.pop("author")
        location_data = data.pop("locations")

        book = Book(**data)

        if author_data:
            author, _created = Author.objects.get_or_create(**author_data)
            book.author = author

        if location_data:
            locations = []
            for location in location_data:
                newLocation, _created = Location.objects.get_or_create(
                    **location)
                locations.append(newLocation)
            book.locations = locations

        book.save()
        return book
