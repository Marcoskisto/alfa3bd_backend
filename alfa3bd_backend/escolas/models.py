from djongo import models


class UnidadeFederativa(models.TextChoices):
    AC = 'AC', 'Acre'
    AL = 'AL', 'Alagoas'
    AP = 'AP', 'Amapá'
    AM = 'AM', 'Amazonas'
    BA = 'BA', 'Bahia'
    CE = 'CE', 'Ceará'
    DF = 'DF', 'Distrito Federal'
    ES = 'ES', 'Espírito Santo'
    GO = 'GO', 'Goiás'
    MA = 'MA', 'Maranhão'
    MT = 'MT', 'Mato Grosso'
    MS = 'MS', 'Mato Grosso do Sul'
    MG = 'MG', 'Minas Gerais'
    PA = 'PA', 'Pará'
    PB = 'PB', 'Paraíba'
    PR = 'PR', 'Paraná'
    PE = 'PE', 'Pernambuco'
    PI = 'PI', 'Piauí'
    RJ = 'RJ', 'Rio de Janeiro'
    RN = 'RN', 'Rio Grande do Norte'
    RS = 'RS', 'Rio Grande do Sul'
    RO = 'RO', 'Rondônia'
    RR = 'RR', 'Roraima'
    SC = 'SC', 'Santa Catarina'
    SP = 'SP', 'São Paulo'
    SE = 'SE', 'Sergipe'
    TO = 'TO', 'Tocantins'


class CategoriaAdministrativa(models.IntegerChoices):
    PRIVADA = 1, 'Privada'
    PUBLICA = 2, 'Publica'


class DependenciaAdministrativa(models.IntegerChoices):
    FEDERAL = 1, 'Federal'
    ESTADUAL = 2, 'Estadual'
    MUNICIPAL = 3, 'Municipal'
    PRIVADA = 4, 'Privada'


class Municipio(models.Model):
    nome = models.CharField(max_length=50)
    unidade_federativa = models.CharField(max_length=2)
    models.UniqueConstraint(
        fields=['nome', 'unidade_federativa'], name='unica_cidade')


class UnidadeEscolar(models.Model):

    codigo_inep = models.IntegerField(unique=True)
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(
        Municipio, on_delete=models.DO_NOTHING)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    categoria_administrativa = models.IntegerField()
    dependencia_administrativa = models.IntegerField()


class Infraestrutura(models.Model):
    nome_cluster = models.CharField(null=False, max_length=30)
    nivel_governamental = models.IntegerField(null=False)
    nome_provedor = models.CharField(null=False, max_length=255)


class Node(models.Model):
    infraestrutura = models.ForeignKey(
        Infraestrutura, on_delete=models.DO_NOTHING, related_name='nodes')
    node_ip = models.CharField(null=False, max_length=15)
    node_port = models.IntegerField(null=False)


class Contrato(models.Model):
    unidade_escolar = models.ForeignKey(
        UnidadeEscolar, on_delete=models.DO_NOTHING, related_name='contratos')
    infraestrutura = models.ForeignKey(
        Infraestrutura, on_delete=models.DO_NOTHING, related_name='contrato')

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    tipo = models.IntegerField(unique=True)


class EscolasCSVFile(models.Model):
    file_data = models.FileField(blank=True, default='')
