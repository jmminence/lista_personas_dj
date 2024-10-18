from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'sexo', 'edad', 'altura', 'peso', 'cintura', 'abdomen']