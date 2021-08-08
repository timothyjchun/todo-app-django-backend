from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.views import APIView
# Create your views here.
from .models import Task
from .serializers import TaskSerializer


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GetTask(APIView):
    serializers = TaskSerializer

    def get(self,request):
        pass


class AddTask(APIView):
    serializers = TaskSerializer

    def post(self,request):
        pass


class DeleteTask(APIView):
    serializers = TaskSerializer
    
    def post(self,request):
        pass

class EditTask(APIView):
    pass