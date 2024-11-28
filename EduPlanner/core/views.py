from django.shortcuts import render
from calendario.views import EventoList
import requests
# Create your views here.
def home(request):
    año = 2024
    datos = getapi(año)

    return render(request, "core/home.html", {"datos": datos})

def getapi(año):
    # url es el nombre que tiene en urls.py
    requests.get(f"http://localhost:8000/holidays/{año}")
    link = requests.get(f"http://localhost:8000/eventos/")

    archivo = link.json()
    print(archivo)
    
    return archivo

