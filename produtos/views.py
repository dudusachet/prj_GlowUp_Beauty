from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Produto, Categoria, Subcategoria

def lista_produtos(request):
    """Funçaõ que renderiza a lista de produtos
    """    
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})


def detalhes_produto(request, id):
    """Função que renderiza os detalhes do produto
    """    
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})


def filtrar_produtos(request):
    """Função que permite realizar o filtro nas categorias de produtos
    """    
    categoria = request.GET.get('categoria')
    produtos = Produto.objects.filter(categoria__nome=categoria)
    data = list(produtos.values())
    return JsonResponse(data, safe=False)


def index(request):
    """Funçaõ que renderiza a página inicial do site apresentando os produtos
    """    
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


def produtos_json(request):
    """Função que retorna os produtos no formato JSON
    """    
    produtos = Produto.objects.all()

    if request.GET.get('categoria_id'):
        produtos = produtos.filter(categoria_id=request.GET['categoria_id'])
    if request.GET.get('subcategoria'):
        produtos = produtos.filter(subcategoria_id=request.GET['subcategoria'])
    if request.GET.get('marca'):
        produtos = produtos.filter(marca=request.GET['marca'])
    if request.GET.get('preco_min'):
        produtos = produtos.filter(preco__gte=request.GET['preco_min'])
    if request.GET.get('preco_max'):
        produtos = produtos.filter(preco__lte=request.GET['preco_max'])

    data = list(produtos.values('id', 'nome', 'marca', 'preco', 'imagem'))
    return JsonResponse(data, safe=False)
