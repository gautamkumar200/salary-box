from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class Coordinates(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    user_id = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=False
    )

    class Meta:
        unique_together = ('x_coordinate', 'y_coordinate',)