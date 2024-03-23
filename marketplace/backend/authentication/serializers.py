from rest_framework import serializers
from users.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer, SetUsernameSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'country', 'city', 'phone_number', 'password']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'owned_products', 'city']


class SetUsernameSerializer(SetUsernameSerializer):
    class Meta(SetUsernameSerializer.Meta):
        fields = ('new_username', 're_new_username', 'current_password')