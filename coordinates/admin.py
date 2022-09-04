from django.contrib import admin
from django.contrib.admin import ModelAdmin

from coordinates.models import Coordinates

# Register your models here.


@admin.register(Coordinates)
class CoordinateAdmin(ModelAdmin):
    list_display = [field.name for field in Coordinates._meta.fields]
