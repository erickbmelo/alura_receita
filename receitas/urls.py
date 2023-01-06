from django.urls import path
from receitas.views import index, receita
from receitas import views

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('busca', views.buscar, name='buscar'),
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),
]

# Outra opção
#from . import views
#urlpatterns = [
#        path('', views.index, name='index'),
#        path('receita', views.receita, name='receita')
#