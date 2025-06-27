from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_usuario(request):
    """Função que renderiza a tela que permite ao usuário realizar o login no site
    """    
    if request.method == 'POST':
        username = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('area_cliente')
        else:
            erro = 'Usuário ou senha inválidos.'
            return render(request, 'usuarios/login.html', {'erro': erro})
    return render(request, 'usuarios/login.html')


@login_required
def area_cliente(request):
    """Função que renderiza a área do cliente. Requer que o cliente esteja logado no site.
    """    
    return render(request, 'usuarios/area_cliente.html')


def cadastro_usuario(request):
    """Função que apresenta o formulário de cadastro para realização de login no site
    """    
    if request.method == 'POST':
        nome = request.POST['nome']
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)
            login(request, user)
            return redirect('area_cliente')

    return render(request, 'usuarios/cadastro.html')


def logout_usuario(request):
    """Função que realiza o logout do site, redirecionando para a página inicial
    """    
    logout(request)
    return redirect('pagina_inicial') 