from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('nome', 'email', 'chapa')
    list_display_links = ('nome', 'email', 'chapa')
    search_fields = ('nome', 'chapa',)
    list_filter = ('chapa', 'nome', 'setor',)
    list_per_page =  10

admin.site.register(Pessoa, ListandoPessoas)

