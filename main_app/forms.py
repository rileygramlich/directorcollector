from django.forms import ModelForm
from .models import Showing, Nomination

class ShowingForm(ModelForm):
    class Meta:
        model = Showing
        fields = ['date', 'name', 'genre']