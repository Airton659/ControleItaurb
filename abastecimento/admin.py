from django.contrib import admin
from .models import Veiculo, Abastecimento, Manutencao


class ListandoVeiculos (admin.ModelAdmin):
    list_display = ('id', 'placa', 'setor', 'ativo')
    list_display_links = ('id', 'placa')
    search_fields = ('placa',)
    list_filter = ('placa', 'marca', 'modelo', 'tipo', 'ano', 'setor', 'ativo',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Veiculo, ListandoVeiculos)

class ListandoAbastecimento (admin.ModelAdmin):
    list_display = ( 'placa', 'data_abastecimento', 'km', 'posto', 'motorista', 'combustivel', 'data_registro')
    list_display_links = ('placa', 'data_abastecimento', 'km', 'posto', 'motorista', 'combustivel', 'data_registro')
    search_fields = ('placa','motorista', 'combustivel',)
    list_filter = ('placa', 'motorista', 'combustivel',)
    list_per_page = 10

admin.site.register(Abastecimento, ListandoAbastecimento)


class ListandoManutencao (admin.ModelAdmin):
    list_display = ('placa', 'data_registro', 'data_manutencao')
    list_display_links = ('placa', 'data_registro', 'data_manutencao')
    search_fields = ('placa','data_registro', 'data_manutencao',)
    list_filter = ('placa','data_registro', 'data_manutencao',)    
    list_per_page = 10

admin.site.register(Manutencao, ListandoManutencao)



 
