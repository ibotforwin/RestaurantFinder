from rest_framework import serializers
from .models import Restaurant, UserData, Location


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name','latitude','longitude', 'rating')


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('id', 'user', 'restaurant', 'blacklisted', 'favorite')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'city')
