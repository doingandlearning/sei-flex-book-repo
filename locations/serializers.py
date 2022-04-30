from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

    def update(self, location, data):
        print(">>>>>>> location books", location.books)
        pass
