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
