from django import forms
from .models import Hike, Comments


class HikeForm(forms.ModelForm):

    class Meta:
        model = Hike
        fields = ('title', 'description', 'street', 'city', 'zipcode')


