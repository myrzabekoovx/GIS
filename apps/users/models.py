from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    is_vendor = models.BooleanField(default=False)  # Для ресторанов/доставщиков

    def __str__(self):
        return self.email