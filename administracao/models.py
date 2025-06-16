from django.db import models
from produtos.models import Produto

class Promocao(models.Model):
    produto = models.ManyToManyField(Produto)
    tipo = models.CharField(max_length=20, choices=[('porcentagem', 'Porcentagem'), ('preco_fixo', 'Preço Fixo')])
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativa = models.BooleanField(default=True)
