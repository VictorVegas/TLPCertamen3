from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
import requests

# Create your views here.

def feriados(request):
    #el link es para pedir a la api de calendarific todos los holiday del 2024
    #respuesta = requests.get("https://calendarific.com/api/v2/holidays?api_key=UokDS8riP0OwL7REfRNJoJOdKp65nWCs&country=CL&year=2024").json()
    return HttpResponse("hola")
