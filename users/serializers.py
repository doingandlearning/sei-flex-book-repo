from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email')

    def create(self, data):
        user = User.objects.create_user(
            data['username'], password=data['password'], first_name=data['first_name'], email=data['email'])

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
