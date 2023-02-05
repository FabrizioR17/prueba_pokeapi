from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
    path('pokedex/', views.pokedexs_list, name='pokedex_list'),
]
