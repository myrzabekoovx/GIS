from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as gis_models

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    location = gis_models.PointField(geography=True)