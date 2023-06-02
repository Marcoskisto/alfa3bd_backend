from django.db import models

# Create your models here.
class Estudante(models.Model):
    cpf = models.CharField(max_length=11)
