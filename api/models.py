from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# We have a country/city model just to narrow down the amount of data we have to query. For example, instead of checking a certain lat and lon against the whole dataset, we can narrow it down to just restaurants in one city within one country.
class Location(models.Model):
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class Restaurant(models.Model):
    # Country and city both have a many to one relationship to the Country model class.
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude=models.FloatField(max_length=32, default=0)
    longitude=models.FloatField(max_length=32, default=0)
    rating=models.FloatField()

class UserData(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blacklisted = models.BooleanField(default=False)
    favorite=models.BooleanField(default=False)
    #
    # class Meta:
    #     unique_together  = (('user','restaurant'),)
    #     index_together  = (('user','restaurant'),)

