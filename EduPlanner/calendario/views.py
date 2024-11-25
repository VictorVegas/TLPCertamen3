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
    
# funcion para obtener los feriados de Chile del 2024 (se puede cambiar el año alterando el url al final &year=año)
def getHolidays(request):
    link = requests.get("https://calendarific.com/api/v2/holidays?api_key=UokDS8riP0OwL7REfRNJoJOdKp65nWCs&country=CL&year=2024")
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
        evento.save()

        for tipo in i.get('type'):
            print(tipo)
            match (tipo):
                case "National holiday":
                    evento.tipos.add(TipoEvento.objects.get(nombre='Feriado Nacional'))
                    break
                case "Common local holiday":
                    evento.tipos.add(TipoEvento.objects.get(nombre='Feriado Nacional'))
                    break
                case "Observance":
                    evento.tipos.add(TipoEvento.objects.get(nombre='Evento'))
                    break
                case "Season":
                    evento.tipos.add(TipoEvento.objects.get(nombre='Temporada'))
                    break
                case "Christian":
                    evento.tipos.add(TipoEvento.objects.get(nombre='Religioso'))
                    break
                case other:
                    print("no encontre el tipo, no se creo el evento " + evento.nombre)
                    break
        
    return redirect('eventos')