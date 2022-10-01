from django.contrib.auth.models import User
from rest_framework import serializers

from coordinates.models import Coordinates


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "email"]


class CoordinatesSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(write_only=True)
    user_name = serializers.CharField(source="user_id.first_name")

    class Meta:
        model = Coordinates
        fields = ["id", "x_coordinate", "y_coordinate", "user_name", "user_id"]


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ("file",)
