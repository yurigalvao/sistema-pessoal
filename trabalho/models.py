from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    
    TIPO_CHOICES = [
        ('socio', 'Sócio'),
        ('percentual', '% do projeto'),
        ('freelancer', 'Freelancer'),
        ('pessoal', 'Pessoal'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='pessoal')
    
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    
    STATUS_CHOICES = [
        ('a_fazer', 'A Fazer'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='a_fazer')
    
    data_vencimento = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Anotacao(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    
    TIPO_CHOICES = [
        ('erro', 'Erro'),
        ('acerto', 'Acerto'),
        ('conceito', 'Conceito'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='conceito')
    
    conteudo = models.TextField(blank=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Anotação"
        verbose_name_plural = "Anotações"

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.conteudo[:30]}"