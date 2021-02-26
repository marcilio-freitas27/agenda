from django.shortcuts import render
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    # lista 1 => evento = Evento.objects.get(id=1)
    # lista todos
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)