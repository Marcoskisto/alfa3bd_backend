# from django.shortcuts import render
from rest_framework import viewsets

from estudantes import models
from estudantes import serializers

# Create your views here.
class Estudante(viewsets.ModelViewSet):
    queryset = models.Estudante.objects.all()
    serializer_class = serializers.EstudanteSerializer
