# from bson.objectid import ObjectId
# import json
# from pymongo import MongoClient
# from django.http import JsonResponse
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def pokemon_list(request):
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['pokeapi_co_db']
#     collection = db['pokemon_v2_pokemon']
#     pokemons = list(collection.find({}))

#     # Recorre todos los pokemons y convierte ObjectId a str
#     for pokemon in pokemons:
#         for key, value in pokemon.items():
#             if isinstance(value, ObjectId):
#                 pokemon[key] = str(value)

#     paginator = Paginator(pokemons, 10) # Mostrar 10 pokemons por página
#     page = request.GET.get('page')

#     try:
#         pokemons = paginator.page(page)
#     except PageNotAnInteger:
#         # Si la página no es un número entero, muestra la primera página
#         pokemons = paginator.page(1)
#     except EmptyPage:
#         # Si la página está fuera del rango, muestra la última página
#         pokemons = paginator.page(paginator.num_pages)

#     data = {'pokemons': list(pokemons)}
#     if pokemons.has_previous():
#         data['previous'] = f'http://127.0.0.1:8000/api/v2/pokemon/?page={pokemons.previous_page_number()}'
#     if pokemons.has_next():
#         data['next'] = f'http://127.0.0.1:8000/api/v2/pokemon/?page={pokemons.next_page_number()}'
    
#     return JsonResponse(data)

from bson.objectid import ObjectId
import json
from pymongo import MongoClient
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pokemon_list(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pokeapi_co_db']
    collection = db['pokemon_v2_pokemon']
    pokemons = list(collection.find({}))

    # Recorre todos los pokemons y convierte ObjectId a str
    for pokemon in pokemons:
        for key, value in pokemon.items():
            if isinstance(value, ObjectId):
                pokemon[key] = str(value)

    paginator = Paginator(pokemons, 10) # Mostrar 10 pokemons por página
    page = request.GET.get('page')

    try:
        pokemons = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, muestra la primera página
        pokemons = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango, muestra la última página
        pokemons = paginator.page(paginator.num_pages)

    pokemons_list = list(pokemons)

    response = {
        
        'previous_page': None,
        'next_page': None,
        'first_page': None,
        'last_page': None,
        'pokemons': pokemons_list,
    }

    if pokemons.has_previous():
        response['previous_page'] = f'/api/v2/pokemon?page={pokemons.previous_page_number()}'

    if pokemons.has_next():
        response['next_page'] = f'/api/v2/pokemon?page={pokemons.next_page_number()}'

    if pokemons.has_previous() or pokemons.has_next():
        response['first_page'] = f'/api/v2/pokemon?page={paginator.page(1).number}'
        response['last_page'] = f'/api/v2/pokemon?page={paginator.page(paginator.num_pages).number}'
        
    return JsonResponse(response)

def pokedex_list(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pokeapi_co_db']
    collection = db['pokemon_v2_pokedex']
    pokedexs = list(collection.find({}))

    # Recorre todos los pokedexs y convierte ObjectId a str
    for pokedex in pokedexs:
        for key, value in pokedex.items():
            if isinstance(value, ObjectId):
                pokedex[key] = str(value)

    paginator = Paginator(pokedexs, 10) # Mostrar 10 pokemons por página
    page = request.GET.get('page')

    try:
        pokedexs = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, muestra la primera página
        pokedexs = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango, muestra la última página
        pokedexs = paginator.page(paginator.num_pages)

    pokedex_list = list(pokedexs)

    response = {
        
        'previous_page': None,
        'next_page': None,
        'first_page': None,
        'last_page': None,
        'pokedexs': pokedex_list,
    }

    if pokedexs.has_previous():
        response['previous_page'] = f'/api/v2/pokedex?page={pokedexs.previous_page_number()}'

    if pokedexs.has_next():
        response['next_page'] = f'/api/v2/pokedex?page={pokedexs.next_page_number()}'

    if pokedexs.has_previous() or pokedexs.has_next():
        response['first_page'] = f'/api/v2/pokedex?page={paginator.page(1).number}'
        response['last_page'] = f'/api/v2/pokedex?page={paginator.page(paginator.num_pages).number}'
        
    return JsonResponse(response)

def pokemon_by_id_name(request, pokemon_identifier):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pokeapi_co_db']
    collection = db['pokemon_v2_pokemon']
    
    try:
        pokemon_id = int(pokemon_identifier)
        pokemon = collection.find_one({'id': pokemon_id})
    except ValueError:
        pokemon = collection.find_one({'name': pokemon_identifier})
    
    if pokemon is None:
        return JsonResponse({'error': f'No se encuentra el Pokemon con el identificador {pokemon_identifier}'})
    
    for key, value in pokemon.items():
        if isinstance(value, ObjectId):
            pokemon[key] = str(value)
    return JsonResponse({'pokemon': pokemon})
