from django.shortcuts import render
from .models import Tarefa 


def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'trabalho/lista_tarefas.html', {'tarefas': tarefas})