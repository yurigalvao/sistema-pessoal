from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='despesa')
    
    def __str__(self):
        return self.nome
    

class Lancamento(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='despesa')
    
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"