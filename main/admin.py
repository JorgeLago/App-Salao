from django.contrib import admin
from main.models import Cliente, Servico, Agendamento

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'whatsapp')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
admin.site.register(Cliente, Clientes)

class Servicos(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor')
    list_display_links = ('id','descricao')
    search_fields = ('descricao',)

admin.site.register(Servico, Servicos)

class Agendamentos(admin.ModelAdmin):
    list_display = ('id', 'servico', 'cliente', 'valor_cobrado','data')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente',)

admin.site.register(Agendamento, Agendamentos)
