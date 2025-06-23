from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('produtos/', views.produtos, name='admin_produtos'),
    path('promocoes/', views.promocoes, name='admin_promocoes'),
    path('promocoes/nova', views.nova_promocao, name='nova_promocao'),
    path('promocoes/<int:promocao_id>/editar/', views.editar_promocao, name='editar_promocao'),
    path('promocoes/<int:promocao_id>/inativar/', views.inativar_promocao, name='inativar_promocao'),
    path('produtos/novo/', views.novo_produto, name='novo_produto'),
    path('produtos/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('produtos/<int:produto_id>/remover/', views.remover_produto, name='remover_produto'),
]