import re
from urllib import response
from django.shortcuts import render
from core.models import Evento
 
# Create your views here.
def login_user(request):
    render (request, 'login.html')

def lista_eventos(request):
    usuario = request.user
    evento=Evento.objects.get (id = 1)
    dados= {'evento':evento}
    return render(request,'agenda.html', dados)