from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True) #serializer accepts passowrd but doesnt give it back
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    bio = serializers.CharField()
    photo = serializers.URLField()
    address = serializers.CharField()

    def create(Self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
