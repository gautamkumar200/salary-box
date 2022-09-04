from rest_framework import serializers

from coordinates.models import Coordinates


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ["id", "x_coordinate", "y_coordinate"]


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)