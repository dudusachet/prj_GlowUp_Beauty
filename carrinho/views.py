
from django.http import JsonResponse
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from produtos.models import Produto


def carrinho(request):
    """Funçaõ que renderiza na tela o carrinho de compras do cliente
    """    
    carrinho = request.session.get('carrinho', {})

    if request.method == 'POST':
        acao = request.POST.get('acao')
        produto_id = request.POST.get('produto_id')
        if produto_id:
            if acao == 'remover':
                carrinho.pop(produto_id, None)
            elif acao == 'atualizar':
                nova_qtd = int(request.POST.get('quantidade', 1))
                carrinho[produto_id] = max(1, nova_qtd)
            request.session['carrinho'] = carrinho
        return redirect('ver_carrinho')

    # exibição dos itens
    produtos = []
    total = 0
    for id_str, qtd in carrinho.items():
        produto = Produto.objects.get(id=int(id_str))
        subtotal = produto.preco * qtd
        produtos.append({
            'produto': produto,
            'quantidade': qtd,
            'subtotal': subtotal,
        })
        total += subtotal

    return render(request, 'carrinho/carrinho.html', {
        'produtos': produtos,
        'total': total,
    })


def adicionar_ao_carrinho(request, produto_id):
    """Função para adicionar um item ao carrinho
    """    
    produto = get_object_or_404(Produto, id=produto_id)

    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1

    request.session['carrinho'] = carrinho
    return redirect('detalhes_produto', id=produto_id)


def carrinho_json(request):
    """Função que retorna o json dos itens no carrinho
    """
    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0

    for id_str, qtd in carrinho.items():
        try:
            produto = Produto.objects.get(id=int(id_str))
            subtotal = produto.preco * qtd
            itens.append({
                'id': produto.id,
                'nome': produto.nome,
                'preco': float(produto.preco),
                'imagem': produto.imagem.url if produto.imagem else '',
                'quantidade': qtd,
                'subtotal': float(subtotal),
            })
            total += subtotal
        except Produto.DoesNotExist:
            continue

    return JsonResponse({'produtos': itens, 'total': float(total)})
