from django.shortcuts import render, redirect
from .models import Carrinho, ItemCarrinho
from produtos.models import Produto
from django.contrib.auth.decorators import login_required

@login_required
def ver_carrinho(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user, finalizado=False)
    return render(request, 'carrinho/carrinho.html', {'carrinho': carrinho})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user, finalizado=False)
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    item.quantidade += 1
    item.preco_unitario = produto.preco
    item.save()
    return redirect('ver_carrinho')
