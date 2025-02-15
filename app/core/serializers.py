from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name','genres','actors']

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'  

class MovieShedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_shedules
        fields = '__all__' 

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'        

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','movie_shedule','seat_type']                         
        read_only_fields = ['id']