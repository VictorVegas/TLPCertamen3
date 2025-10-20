from rest_framework import generics, status
from rest_framework.response import Response
from .models import Evento, TipoEvento
from .serializers import eventoSerializer, tipoEventoSerializer
from datetime import date
from django.shortcuts import redirect
import requests

# vista de la lista de eventos
class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = eventoSerializer

    def delete (self, request, *args, **kwargs):
        Evento.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# vista de detalle de evento
class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = eventoSerializer

# vista de lista de tipos de eventos
class TipoEventoList(generics.ListCreateAPIView):
    queryset = TipoEvento.objects.all()
    serializer_class = tipoEventoSerializer

# vista de detalle de tipo de evento
class TipoEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoEvento.objects.all()
    serializer_class = tipoEventoSerializer
    
# vista para obtener los feriados de Chile del año solicitado
def getHolidays(request, year):
    link = requests.get(f"https://calendarific.com/api/v2/holidays?api_key=UokDS8riP0OwL7REfRNJoJOdKp65nWCs&country=CL&year={year}")
    archivo = link.json()
    response = archivo.get("response")
    holidays = response.get('holidays')
    for i in holidays:
        evento = Evento()
        evento.nombre = i.get('name')
        fecha = i.get('date')
        datetime = fecha.get('datetime')
        year = datetime.get('year')
        month = datetime.get('month')
        day = datetime.get('day')
        evento.fecha = date(year, month, day)
        evento.descripcion = i.get('description')
        

        for tipo in i.get('type'):
            evento.tipos.append(tipo)
        evento.save()
        
    return redirect('eventos')
        
    