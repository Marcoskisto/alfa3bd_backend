# Serializers define the API representation.
from rest_framework import serializers
from estudantes import models


class EstudanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Estudante
        fields = ['cpf']
