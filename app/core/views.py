from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class ActorView(APIView):
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]

    
    def get(self,request,pk=None):
        if pk:
            try:
                actor = Actors.objects.get(pk=pk) 
            except Actors.DoesNotExist:   
                return Response(status=status.HTTP_404_NOT_FOUND)  
            serializer = ActorSerializer(actor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        actor = Actors.objects.all()  
        serializer = ActorSerializer(actor,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New Actor Created!"},status=status.HTTP_201_CREATED)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
           actor = Actors.objects.get(pk=pk)
        except Actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        serializer = ActorSerializer(actor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        try:
            actor = Actors.objects.get(pk=pk)
        except Actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MovieView(APIView):
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    
    def get(self,request,pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk) 
            except Movie.DoesNotExist:   
                return Response(status=status.HTTP_404_NOT_FOUND)  
            serializer = MovieSerializer(movie)
            return Response(serializer.data,status=status.HTTP_200_OK)
        movie = Movie.objects.all()  
        serializer = ActorSerializer(movie,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New Movie Created!"},status=status.HTTP_201_CREATED)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
           movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    
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
        serializer = ActorSerializer(theatre,many=True)
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


