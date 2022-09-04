from django.urls import path

from coordinates.views import coordinates_view, bulk_coordinate_upload_view

urlpatterns = [

    path('', view=coordinates_view, name="coordinates"),
    path('bulk-upload', view=bulk_coordinate_upload_view, name="bulk_coordinates"),
]

