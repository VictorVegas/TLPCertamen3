from rest_framework import serializers
from .models import *

class eventoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Evento
        fields = '__all__'

class tipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = '__all__'