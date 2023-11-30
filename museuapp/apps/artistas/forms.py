from django import forms
from .models import Artista

class ArtistaForm(forms.ModelForm):

    class Meta:
        model = Artista
        exclude = ('created_on' , 'updated_on',)