import pandas as pd
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response

from coordinates.models import Coordinates
from coordinates.serializers import CoordinatesSerializer, FileUploadSerializer
from rest_framework.permissions import IsAuthenticated

from salary_box_task.utils import BearerAuthentication


# Create your views here.


@api_view(["GET", "POST"])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
@cache_page(timeout=60000, key_prefix="coordinates")
def coordinates_view(request):
    if request.method == "GET":
        if True:
            # coordinates = cache.get("coordinates")
            # if not coordinates:
                coordinates = Coordinates.objects.filter(user_id=request.user)
            #     cache.set("coordinates", coordinates, timeout=None)
            #     print("-------------database------------")
            # # else:
            #     print("-------------cache------------")
        else:
            #@TODO for group leader show the all coordinates
            coordinates = Coordinates.objects.filter()
        serialized_data = CoordinatesSerializer(coordinates, many=True)
        return Response(serialized_data.data)
    elif request.method == "POST":
        serializer = CoordinatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data.update({"user_id": request.user})
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def bulk_coordinate_upload_view(request):
    serializer = FileUploadSerializer(data=request.data)
    if serializer.is_valid():
        try:
            file = serializer.validated_data["file"]
            reader = pd.read_csv(file)
            for _, row in reader.iterrows():
                coordinate = Coordinates(
                    x_coordinate=int(row["x_coordinate"]),
                    y_coordinate=int(row["y_coordinate"]),
                    user_id=request.user,
                )
                coordinate.save()
            return Response(
                "Coordinates have been stored successfully",
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                "Failed to save coordinates. Reason- {}".format(str(e)),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    return Response(status=status.HTTP_400_BAD_REQUEST)
