from django.shortcuts import render
from calendario.views import EventoList
import requests
# Create your views here.
def home(request):

    return render(request, "core/home.html")

def getapi(request, año):
    # url es el nombre que tiene en urls.py
    requests.get(f"http://localhost:8000/holidays/{año-1}")
    requests.get(f"http://localhost:8000/holidays/{año}")
    requests.get(f"http://localhost:8000/holidays/{año+2}")
    link = requests.get(f"http://localhost:8000/eventos/")

    archivo = link.json()
    return archivo

