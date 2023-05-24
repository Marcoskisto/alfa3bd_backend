import pandas as pd
from unidecode import unidecode
from escolas import models


def update_database(csv_file):
    """ Atualiza o banco de dados com os dados 
    das Escolas fornecidos por um arquivo csv

    Args:
        csv_file (file_path): _description_
    """
    file = pd.read_csv(
        filepath_or_buffer=csv_file,
        sep=';',
        encoding='utf-8')

    for i in range(0, len(file)):

        _uf_sigla = file['UF'][i].upper()
        unid_federativa = models.UnidadeFederativa[_uf_sigla]

        municipio_nome = unidecode(file['Município'][i]).upper()
        municipio, _ = models.Municipio.objects.get_or_create(
            **{
            'nome':municipio_nome,
            'unidade_federativa': unid_federativa.value
            }
        )

        codigo_inpe = file['Código INEP'][i]
        nome_escola = file['Escola'][i]
        _cat_adm = unidecode(file['Categoria Administrativa'][i]).upper()
        categoria_admin = models.CategoriaAdministrativa[_cat_adm]
        endereco = file['Endereço'][i]
        telefone = file['Telefone'][i]
        _dep_adm = unidecode(file['Dependência Administrativa'][i]).upper()
        dependencia_admin = models.DependenciaAdministrativa[_dep_adm]

        unidade_escolar = models.UnidadeEscolar.objects.get_or_create(
            codigo_inep=codigo_inpe,
            nome=nome_escola,
            municipio=municipio,
            endereco=endereco,
            telefone=telefone,
            categoria_administrativa=categoria_admin,
            dependencia_administrativa=dependencia_admin
        )[0]
        unidade_escolar.save()

        print(f'Linha: {i} - COD INEP: {unidade_escolar.codigo_inep}')
