from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

    def update(self, location, data):
        location.name = data.get("name", location.name)
        location.save()

        return location
