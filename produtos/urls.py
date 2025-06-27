from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('produtos-json/', views.produtos_json, name='produtos_json'),
    path('produto/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('api/filtrar-produtos/', views.filtrar_produtos, name='filtrar_produtos'),

]
