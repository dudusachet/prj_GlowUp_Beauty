from django import forms
from .models import Promocao

class PromocaoForm(forms.ModelForm):
    class Meta:
        model = Promocao
        fields = ['produto', 'tipo', 'valor', 'data_inicio', 'data_fim']
        widgets = {
            'produto': forms.CheckboxSelectMultiple(),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }
