from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name="itens", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)
