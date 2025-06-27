from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from produtos.models import Produto, Categoria, Subcategoria
from .forms import PromocaoForm
from .forms import ProdutoForm
from .models import Promocao
from datetime import date

def dashboard(request):
    """Função para retornar o dashboard do painel administrativo do site
    """    
    produtos = Produto.objects.all()
    produtos_vencendo = Produto.objects.filter(validade__lte=date.today())
    return render(request, 'administracao/dashboard.html', {
        'produtos': produtos,
        'vencendo': produtos_vencendo,
    })


def produtos(request):
    """Função para renderizar a lista de produtos no painel administrativo
    """    
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    categoria_id = request.GET.get('categoria')

    produtos = Produto.objects.all()

    if data_inicio and data_fim:
        produtos = produtos.filter(validade__range=[data_inicio, data_fim])

    if categoria_id and categoria_id != '':
        produtos = produtos.filter(categoria__id=categoria_id)

    categorias = Categoria.objects.all()

    return render(request, 'administracao/produtos.html', {
        'produtos': produtos,
        'categorias': categorias,
        'filtro_data_inicio': data_inicio,
        'filtro_data_fim': data_fim,
        'filtro_categoria': int(categoria_id) if categoria_id else '',
    })
   
    
def nova_promocao(request):
    """Função que permite cadastrar uma nova promoção
    """    
    if request.method == 'POST':
        form = PromocaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PromocaoForm()
    return render(request, 'administracao/nova_promocao.html', {'form': form})

def editar_promocao(request, promocao_id):
    """Função que permite editar a promoção
    """    
    promocao = get_object_or_404(Promocao, id=promocao_id)
    if request.method == 'POST':
        form = PromocaoForm(request.POST, instance=promocao)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PromocaoForm(instance=promocao)
    return render(request, 'administracao/nova_promocao.html', {'form': form})


def inativar_promocao(request, promocao_id):
    """Função que permite inativar uma promoção
    """  
    promocao = get_object_or_404(Promocao, id=promocao_id)
    promocao.ativa = False
    promocao.save()
    return redirect('admin_dashboard')


def promocoes(request):
    """Função que retorna as promoções do site
    """  
    promocoes_ativas = Promocao.objects.filter(ativa=True)
    promocoes_inativas = Promocao.objects.filter(ativa=False)
    return render(request, 'administracao/promocoes.html', {
        'ativas': promocoes_ativas,
        'inativas': promocoes_inativas,
    })
    

def novo_produto(request):
    """Função que permite cadastrar um novo produto no site
    """    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)

            # Criar nova categoria, se for o caso
            nova_categoria = form.cleaned_data.get('nova_categoria')
            if nova_categoria:
                categoria = Categoria.objects.create(nome=nova_categoria)
                produto.categoria = categoria
            else:
                categoria = form.cleaned_data.get('categoria')

            # Criar nova subcategoria, se for o caso
            nova_sub = form.cleaned_data.get('nova_subcategoria')
            if nova_sub:
                subcategoria = Subcategoria.objects.create(
                    nome=nova_sub,
                    categoria=produto.categoria or categoria
                )
                produto.subcategoria = subcategoria
            else:
                produto.subcategoria = form.cleaned_data.get('subcategoria')

            produto.save()
            return redirect('admin_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'administracao/form_produto.html', {'form': form, 'titulo': 'Novo Produto'})


def editar_produto(request, produto_id):
    """Função para editar o cadastro de um produto listado no site
    """    
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('admin_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'administracao/form_produto.html', {'form': form, 'titulo': 'Editar Produto'})


def remover_produto(request, produto_id):
    """Função que permite remover um produto do site
    """    
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('admin_produtos')
