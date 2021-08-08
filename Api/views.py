# Create your views here.
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Task
from .serializers import TaskSerializer


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GetTaskView(APIView):
    serializer_class = TaskSerializer

    def get(self,request,format = None):
        tasks = Task.objects.all()
        return JsonResponse(tasks)


class AddTaskView(APIView):
    serializer_class = TaskSerializer

    def post(self,request,format = None):
        serializer = self.serializer_class(request.data)


class DeleteTaskView(APIView):
    serializer_class = TaskSerializer
    
    def post(self,request,format = None):
        pass

class EditTaskView(APIView):
    pass