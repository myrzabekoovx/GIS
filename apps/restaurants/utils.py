from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from apps import restaurants


def get_nearest_restaurants(latitude, longitude, max_distance_km=5):
    user_location = Point(float(longitude), float(latitude), srid=4326)
    return restaurants.objects.annotate(
        distance=Distance('location', user_location)
    ).filter(
        distance__lte=max_distance_km * 1000,
        is_active=True
    ).order_by('distance')