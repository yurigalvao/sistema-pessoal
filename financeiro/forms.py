from django import forms
from .models import Lancamento

class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['categoria', 'tipo', 'valor', 'descricao', 'data']