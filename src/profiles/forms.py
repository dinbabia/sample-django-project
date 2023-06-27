from django import forms

from .models import Profiles

class ProfileModelForm(forms.ModelForm):
    

    class Meta:
        model = Profiles
        fields = ['name', 'age', 'job', 'favorite_sport']
