from django.db import models
from django.core.validators import MinValueValidator


class Restaurant(models.Model):
    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('japanese', 'Japanese'),
        ('american', 'American'),
        ('mexican', 'Mexican'),
        ('russian', 'Russian'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    cuisine_type = models.CharField(max_length=50, choices=CUISINE_CHOICES)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    delivery_radius = models.IntegerField(help_text="Delivery radius in meters")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]

    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[ MinValueValidator(0) ])
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes")

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"