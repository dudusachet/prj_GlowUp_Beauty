
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App produtos
    path('', include('produtos.urls')),

    # App usuários
    path('usuarios/', include('usuarios.urls')),

    # App carrinho
    path('carrinho/', include('carrinho.urls')),

    # App administração
    path('painel/', include('administracao.urls')),
]

