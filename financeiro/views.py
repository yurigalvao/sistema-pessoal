from django.shortcuts import render, redirect
from .models import Lancamento
from .forms import LancamentoForm

def lista_lancamentos(request):
    lancamentos = Lancamento.objects.all()
    return render(request, 'financeiro/lista_lancamentos.html', {'lancamentos': lancamentos})

def criar_lancamento(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_lancamentos')
    else:
        form = LancamentoForm()
    return render(request, 'financeiro/criar_lancamento.html', {'form': form})


def editar_lancamento(request, lancamento_id):
    lancamento = Lancamento.objects.get(id=lancamento_id)
    if request.method == 'POST':
        form = LancamentoForm(request.POST, instance=lancamento)
        if form.is_valid():
            form.save()
            return redirect('lista_lancamentos')
    else:
        form = LancamentoForm(instance=lancamento)
    return render(request, 'financeiro/editar_lancamento.html', {'form': form, 'lancamento': lancamento})

def deletar_lancamento(request, lancamento_id):
    lancamento = Lancamento.objects.get(id=lancamento_id)
    if request.method == 'POST':
        lancamento.delete()
        return redirect('lista_lancamentos')
    return render(request, 'financeiro/deletar_lancamento.html', {'lancamento': lancamento})