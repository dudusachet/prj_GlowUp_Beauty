from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('produto/<int:id>/', views.detalhe_produto, name='produto_detalhe'),
    path('api/filtrar-produtos/', views.filtrar_produtos, name='filtrar_produtos'),
    path('produto/<int:id>/', views.detalhe_produto, name='produto_detalhe'),
]
