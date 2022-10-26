from django.contrib import admin
from .models import Veiculo

class ListandoVeiculos (admin.ModelAdmin):
    list_display = ('id', 'placa', 'setor', 'ativo')
    list_display_links = ('id', 'placa')
    search_fields = ('placa',)
    list_filter = ('placa', 'marca', 'modelo', 'tipo', 'ano', 'setor', 'ativo',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Veiculo, ListandoVeiculos)


