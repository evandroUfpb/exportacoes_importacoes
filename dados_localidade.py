import pandas as pd
import glob

import os, ssl
from tkinter.font import names
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


# funções para ler os arquivos com os dados das exportações e importações
# faz a concatenação das tabelas de exportação e imortações (2012 a 2021),
# criando um data frama geral para exporação e outro para importação 


list_col = ['CO_ANO','CO_MES','CO_NCM','CO_PAIS','SG_UF_NCM','CO_VIA','VL_FOB']

def exportacoes():
    exportacoes = glob.glob('dados/EXP*.csv')
    array_exp = []
    for x in exportacoes:
        temp_exp = pd.read_csv(x, sep=';', usecols=list_col)
        array_exp.append(temp_exp)
    return pd.concat(array_exp, axis=0)    

def importacoes():
    importacoes = glob.glob('dados/IMP*.csv')
    array_imp = []
    for x in importacoes:
        temp_imp = pd.read_csv(x, sep=';', usecols=list_col)
        array_imp.append(temp_imp)
    return pd.concat(array_imp, axis=0) 
    

# Cria os data frames necessários para cruzamento com os dados de exportações e importações
def paises():
    url_paises = 'https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv'
    paises = pd.read_csv(url_paises, sep=';', encoding='iso-8859-1', index_col='CO_PAIS', usecols=['CO_PAIS', 'NO_PAIS', 'CO_PAIS_ISOA3'])
    return paises

def estados():
    url_estados = 'https://balanca.economia.gov.br/balanca/bd/tabelas/UF.csv'
    estados = pd.read_csv(url_estados, sep=';', encoding='iso-8859-1', index_col='CO_UF')
    return estados

def municipios():
    url_municipios = 'https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv'
    municipios = pd.read_csv(url_municipios, sep=';', encoding='iso-8859-1')
    return municipios

def ncm():
    url_ncm = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv'
    df_ncm = pd.read_csv(url_ncm, sep=';', encoding='iso-8859-1', index_col='CO_NCM', usecols=['CO_NCM','CO_CGCE_N3'])
    return df_ncm

def cat_economica():
    url_cat_economica = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_CGCE.csv'
    cat_economica = pd.read_csv(url_cat_economica, sep=';', encoding='iso-8859-1', index_col='CO_CGCE_N3', usecols=['CO_CGCE_N3','NO_CGCE_N3'])
    return cat_economica

