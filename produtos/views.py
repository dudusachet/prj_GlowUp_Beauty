from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})

def filtrar_produtos(request):
    categoria = request.GET.get('categoria')
    produtos = Produto.objects.filter(categoria__nome=categoria)
    data = list(produtos.values())
    return JsonResponse(data, safe=False)
