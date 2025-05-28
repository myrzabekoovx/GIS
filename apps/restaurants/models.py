from django.contrib.gis.db import models as gis_models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.PointField(geography=True)
    address = models.TextField()
    delivery_radius = models.IntegerField()  # в метрах

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)