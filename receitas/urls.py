from django.urls import path
from receitas.views import index, receita

urlpatterns = [
        path('', index, name='index'),
        path('receita', receita, name='receita')
]

# Outra opção
#from . import views
#urlpatterns = [
#        path('', views.index, name='index'),
#        path('receita', views.receita, name='receita')
#]