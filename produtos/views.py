from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Produto, Categoria, Subcategoria

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})


def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})


def filtrar_produtos(request):
    categoria = request.GET.get('categoria')
    produtos = Produto.objects.filter(categoria__nome=categoria)
    data = list(produtos.values())
    return JsonResponse(data, safe=False)


def index(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.filter(pai__isnull=True)
    marcas = Produto.objects.values_list('marca', flat=True).distinct()
    subcategorias = Subcategoria.objects.all()

    # Filtros do usuário
    categoria_id = request.GET.get('categoria_id')  # clicada na barra lateral
    marca = request.GET.get('marca')
    subcategoria_id = request.GET.get('subcategoria')
    preco_min = request.GET.get('preco_min')
    preco_max = request.GET.get('preco_max')

    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    if subcategoria_id:
        produtos = produtos.filter(subcategoria_id=subcategoria_id)
    if marca:
        produtos = produtos.filter(marca=marca)
    if preco_min:
        produtos = produtos.filter(preco__gte=preco_min)
    if preco_max:
        produtos = produtos.filter(preco__lte=preco_max)

    context = {
        'produtos': produtos,
        'categorias': categorias,
        'subcategorias': subcategorias,
        'marcas': marcas,
        'filtro_marca': marca,
        'filtro_subcategoria': subcategoria_id,
        'preco_min': preco_min,
        'preco_max': preco_max,
    }
    return render(request, 'produtos/index.html', context)
