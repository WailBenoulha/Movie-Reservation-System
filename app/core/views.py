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