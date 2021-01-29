from django.contrib import admin
from core.models import Evento
# Register your models here.
# registrar suas classes e models

#classe de administração
class EventoAdmin(admin.ModelAdmin):
    # campos para aparecer no django admin
    list_display = ('titutlo','data_evento','data_criacao')
    #filtro de titulos e demais conteudos
    list_filter = ('usuario','data_evento',)

admin.site.register(Evento, EventoAdmin)