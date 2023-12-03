from django import forms
from .models import Entidade

class EntidadeForm(forms.ModelForm):

    class Meta:
        model = Entidade
        exclude = ('created_on' , 'updated_on',)