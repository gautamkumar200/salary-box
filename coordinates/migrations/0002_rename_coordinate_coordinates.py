# Generated by Django 3.2.11 on 2022-09-04 05:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coordinates', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coordinate',
            new_name='Coordinates',
        ),
    ]
