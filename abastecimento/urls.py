from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name='logout'),
    path('veiculos', views.veiculos, name='veiculos'),
    path('<int:veiculo_id>', views.veiculo, name='veiculo'),
    path('buscar', views.buscar, name='buscar'),
    path('abastecimentos', views.todos_abastecimentos, name='todos_abastecimentos'),
    path('manutencoes', views.manutencoes, name='manutencoes'),
    path('abastecimento', views.adiciona_abastecimento, name='abastecimento'),    
    path('<int:veiculo_id>/abastecimentos', views.busca_abastecimentos, name='busca_abastecimentos'),    
    # path('manutencao', views.adiciona_manutencao, name='manutencao'),    
    # path('<int:veiculo_id>/manutencoes', views.busca_manutencoes, name='busca_manutencoes'),
    ]