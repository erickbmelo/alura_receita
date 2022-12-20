from django.urls import path
from receitas.views import index, receita
from receitas import views

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('busca', views.buscar, name='buscar')
]

# Outra opção
#from . import views
#urlpatterns = [
#        path('', views.index, name='index'),
#        path('receita', views.receita, name='receita')
#