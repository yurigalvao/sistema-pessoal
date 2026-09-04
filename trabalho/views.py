from django.shortcuts import render, redirect
from .models import Tarefa 
from .forms import TarefaForm


def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'trabalho/lista_tarefas.html', {'tarefas': tarefas})


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'trabalho/criar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'trabalho/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def deletar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'trabalho/deletar_tarefa.html', {'tarefa': tarefa})