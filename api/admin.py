from django.contrib import admin
from .models import Restaurant, UserData, Location
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(UserData)
admin.site.register(Location)