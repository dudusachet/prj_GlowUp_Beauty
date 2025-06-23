
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

