from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated


class ActorListView(ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]
    
class ActorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]   

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]       

class TheatreView(APIView):
    serializer_class = TheatreSerializer
    permission_classes = [AllowAny]

    
    def get(self,request,pk=None):
        if pk:
            try:
                theatre = Theatre.objects.get(pk=pk) 
            except Theatre.DoesNotExist:   
                return Response(status=status.HTTP_404_NOT_FOUND)  
            serializer = TheatreSerializer(theatre)
            return Response(serializer.data,status=status.HTTP_200_OK)
        theatre = Theatre.objects.all()  
        serializer = TheatreSerializer(theatre,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TheatreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New Theatre Created!"},status=status.HTTP_201_CREATED)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
           theatre = Theatre.objects.get(pk=pk)
        except Theatre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        serializer = TheatreSerializer(theatre,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        try:
            theatre = Theatre.objects.get(pk=pk)
        except Theatre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        theatre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class MovieSheduleView(APIView):
    queryset = Movie_shedules.objects.all()
    serializer_class = MovieShedulesSerializer
    permission_classes = [AllowAny]

    def get(self,request):
        model = Movie_shedules.objects.all()
        serializer = MovieShedulesSerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = MovieShedulesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
@permission_classes([AllowAny])
def get_seats(request,pk=None):
    if pk:
        try:
            model = Seats.objects.get(pk=pk)
            serializer = SeatsSerializer(model)
        except Movie_shedules.DoesNotExist:
            return Response({'error':'Seat not found'},status=status.HTTP_404_NOT_FOUND)
            
    model = Seats.objects.all()
    serializer = SeatsSerializer(model,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

from rest_framework.generics import CreateAPIView
class TicketView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]

from django.contrib.auth.models import Group,Permission  

class TicketsView(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer    
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
      