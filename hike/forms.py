from django import forms
from .models import Hike, Comments


#class DateInput(forms.DateInput):
 #   input_type = 'date'
 
class HikeForm(forms.ModelForm):

    class Meta:
        model = Hike
        #hike_date = forms.DateField(widget=DateInput()
       # widgets = {'hike_date' : DateInput()}
        fields = ('title', 'description', 'street', 'city', 'zipcode', 'hike_date', 'distance', 'picture', 'difficulty')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('body', 'rating')




