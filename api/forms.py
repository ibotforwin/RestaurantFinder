from django import forms
from .models import UserData, Location, Restaurant

class LocationForm(forms.ModelForm):
    country = forms.CharField(required=True,)
    city = forms.CharField(required=True)
    class Meta:
        model = Location
        fields = '__all__'