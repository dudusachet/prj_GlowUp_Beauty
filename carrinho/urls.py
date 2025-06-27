from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho-json/', views.carrinho_json, name='carrinho_json'),

]
