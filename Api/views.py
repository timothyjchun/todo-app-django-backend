# Create your views here.
from re import S
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, response
from .models import Task
from .serializers import TaskSerializer


class TaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GetTaskView(APIView):
    serializer_class = TaskSerializer

    def get(self,request,format = None):
        tasks = Task.objects.all()
        serializered = self.serializer_class(tasks,many = True).data
        return Response(serializered)


class AddTaskView(APIView):
    serializer_class = TaskSerializer

    def post(self,request,format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            context = serializer.data.get('context')
            color = serializer.data.get('color')
            new_task = Task(context = context, color = color)
            new_task.save()
            return Response(status = status.HTTP_200_OK)
        else:
            print(serializer.errors)
            # return Response(status = status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors)



class DeleteTaskView(APIView):
    serializer_class = TaskSerializer
    
    def post(self,request,format = None):
        obj = Task.objects.filter(id = request.data["id"]).delete()
        return Response(status = status.HTTP_200_OK)
        


class EditTaskView(APIView):
    pass