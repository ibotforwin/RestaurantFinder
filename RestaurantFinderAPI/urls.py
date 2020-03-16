"""RestaurantFinderAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from api.views import index, profile_view, blacklist, favorite, unblacklist, unfavorite

urlpatterns = [
    path('', index, name='index'),
    path('<str:username>', profile_view, name='profile_view'),
    path('finder/', index, name='finder'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('blacklist/<int:pk>', blacklist, name='blacklist'),
    path('favorite/<int:pk>', favorite, name='favorite'),
    path('unblacklist/<int:pk>', unblacklist, name='unblacklist'),
    path('unfavorite/<int:pk>', unfavorite, name='unfavorite'),
]
