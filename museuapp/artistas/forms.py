from django import forms
from .models import Artistas

class ArtistasForm(forms.ModelForm):

    class Meta:
        model = Artistas
        exclude = ('created_on' , 'updated_on',)