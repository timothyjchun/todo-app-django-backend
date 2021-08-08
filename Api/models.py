from django.db import models

# Create your models here.

class Task(models.Model):
    context = models.TextField(max_length=150,unique=True,null=False)
    color = models.TextField(max_length=50,null=False)