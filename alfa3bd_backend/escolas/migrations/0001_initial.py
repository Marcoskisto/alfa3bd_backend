# Generated by Django 4.1.8 on 2023-05-22 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EscolasCSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_data', models.FileField(blank=True, default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Infraestrutura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cluster', models.CharField(max_length=30)),
                ('nivel_governamental', models.IntegerField()),
                ('nome_provedor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('unidade_federativa', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_inep', models.IntegerField(unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=50)),
                ('categoria_administrativa', models.IntegerField()),
                ('dependencia_administrativa', models.IntegerField()),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolas.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_ip', models.CharField(max_length=15)),
                ('node_port', models.IntegerField()),
                ('infraestrutura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='nodes', to='escolas.infraestrutura')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('tipo', models.IntegerField(unique=True)),
                ('infraestrutura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contrato', to='escolas.infraestrutura')),
                ('unidade_escolar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contratos', to='escolas.unidadeescolar')),
            ],
        ),
    ]
