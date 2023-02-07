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
from django.shortcuts import render
from bson.objectid import ObjectId
import json
from pymongo import MongoClient
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

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

def pokedex_by_id_name(request, pokedex_identifier):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pokeapi_co_db']
    collection = db['pokemon_v2_pokedex']
    
    try:
        pokedex_id = int(pokedex_identifier)
        pokedex = collection.find_one({'id': pokedex_id})
    except ValueError:
        pokedex = collection.find_one({'name': pokedex_identifier})
    
    if pokedex is None:
        return JsonResponse({'error': f'No se encuentra el Pokedex con el identificador {pokedex_identifier}'})
    
    for key, value in pokedex.items():
        if isinstance(value, ObjectId):
            pokedex[key] = str(value)
    return JsonResponse({'pokedex': pokedex})


def register(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["pokeapi_co_db"]
    collection = db["app_pokeapi_user"]

    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if username and password and email:
            if collection.find_one({'username': username}):
                return JsonResponse({'error': 'Username already exists'})
            else:
                unique_id = str(uuid.uuid4())
                collection.insert_one({
                    '_id': unique_id,
                    'username': username,
                    'password': password,
                    'email': email
                })
                return JsonResponse({'message': 'User registered successfully'})
        else:
            return JsonResponse({'error': 'Please provide all required fields'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
