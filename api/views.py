from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Restaurant, UserData
from .serializers import RestaurantSerializer, UserDataSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from .forms import LocationForm
# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    # @action(detail=True, methods=['POST'])
    # def rate_restaurant(self, request, pk=None):
    #     if 'rating' in request.data:
    #         rating=request.data['rating']
    #         restaurant = Restaurant.objects.get(id=pk)
    #         user=User.objects.get(id=1)
    #         print('user', user.username)
    #         print(restaurant.name)
    #
    #         try:
    #             rating_object = Rating.objects.get(user=user, restaurant=restaurant.id)
    #             rating_object.rating = rating
    #             rating_object.save()
    #         except:
    #             rating_object = Rating.objects.create(user=user, restaurant=restaurant.id, rating_object=rating)
    #
    #         response = {'message': 'its working'}
    #         return Response(response, status=status.HTTP_200_OK)
    #     else:
    #         response = {'message': 'You need to provide a rating.'}
    #         return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

def index(request):
    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        print(form)
        if form.is_valid():

            print('test')
            country=form.cleaned_data['country']
            city=form.cleaned_data['city']

            print(country)
            print(city)

            # Get all restaurants which are not blacklisted by the current user within the specified Country and City
            restaurants = Restaurant.objects.filter(location__country=country, location__city=city, userdata__blacklisted=False)

            return render(request, 'api/finder.html', {'restaurants': restaurants})

        else:
            print(form.errors.as_data())
            form = LocationForm()
            print('enter else')


    return render(request, 'api/index.html', {'form':form})

def profile_view(request, username):
    u = User.objects.get(username=username)
    user_data=UserData.objects.all()

    return render(request, 'api/user.html', {'user_data':user_data})