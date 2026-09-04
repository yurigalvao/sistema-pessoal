from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:tarefa_id>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
]