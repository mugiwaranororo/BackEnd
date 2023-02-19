from django import forms
from .models import Sunglasses

#to create and update the form for the sunglasses
class SunglassesForm(forms.ModelForm):
    class Meta:
        model = Sunglasses
        fields = ('name', 'brand', 'color', 'type', 'image')