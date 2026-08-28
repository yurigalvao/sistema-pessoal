from django.contrib import admin
from .models import Projeto, Tarefa, Anotacao
# Register your models here.

admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Anotacao)