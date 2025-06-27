from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.cadastro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('area-cliente/', views.area_cliente, name='area_cliente'),
    path('logout/', views.logout_usuario, name='logout'),

]
