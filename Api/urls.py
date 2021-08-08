from django.urls import path
from .views import TaskView, GetTaskView,AddTaskView,DeleteTaskView

urlpatterns = [
    path('view_task',TaskView.as_view()),
    path('get',GetTaskView.as_view()),
    path('add',AddTaskView.as_view()),
    path('delete',DeleteTaskView.as_view()),
]