from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_lancamentos, name='lista_lancamentos'),
    path('nova/', views.criar_lancamento, name='criar_lancamento'),
    path('<int:lancamento_id>/editar/', views.editar_lancamento, name='editar_lancamento'),
    path('<int:lancamento_id>/deletar/', views.deletar_lancamento, name='deletar_lancamento'),
]