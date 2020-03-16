from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import RestaurantViewSet, UserDataViewSet

router=routers.DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('userdata', UserDataViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
