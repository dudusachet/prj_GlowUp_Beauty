from django import forms
from .models import Promocao
from produtos.models import Produto, Categoria, Subcategoria

class PromocaoForm(forms.ModelForm):
    class Meta:
        model = Promocao
        fields = ['produto', 'tipo', 'valor', 'data_inicio', 'data_fim']
        widgets = {
            'produto': forms.CheckboxSelectMultiple(),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

class ProdutoForm(forms.ModelForm):
    nova_categoria = forms.CharField(required=False, label="Nova Categoria")
    nova_subcategoria = forms.CharField(required=False, label="Nova Subcategoria")

    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'subcategoria', 'marca', 'preco', 'validade', 'cor', 'estoque', 'imagem']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get("categoria")
        nova_categoria = cleaned_data.get("nova_categoria")
        subcategoria = cleaned_data.get("subcategoria")
        nova_subcategoria = cleaned_data.get("nova_subcategoria")

        # Validação: se a nova subcategoria for informada, deve ter uma categoria
        if nova_subcategoria and not (subcategoria or categoria or nova_categoria):
            raise forms.ValidationError("Selecione ou crie uma categoria para a nova subcategoria.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].required = False
        self.fields['subcategoria'].required = False
