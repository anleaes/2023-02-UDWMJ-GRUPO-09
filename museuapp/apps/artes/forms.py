from django import forms
from .models import Arte

class ArteForm(forms.ModelForm):

    class Meta:
        model = Arte
        exclude = ('created_on' , 'updated_on',)