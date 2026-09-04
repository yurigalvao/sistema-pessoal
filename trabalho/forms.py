from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['projeto', 'titulo', 'descricao', 'prioridade', 'status', 'data_vencimento']