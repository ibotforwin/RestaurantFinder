from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserData, Location, Restaurant
from django.utils.translation import ugettext_lazy as _

from django.core.validators import RegexValidator


class LocationForm(forms.ModelForm):
    country = forms.CharField(required=True,)

    city = forms.CharField(required=True)



    class Meta:
        model = Location
        fields = '__all__'