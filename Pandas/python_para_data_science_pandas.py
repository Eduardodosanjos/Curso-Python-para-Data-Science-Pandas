# -*- coding: utf-8 -*-
"""Python_para_Data_Science_Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UAHu1yauN8QGfWa2X_Py8icEP8gDRo2l

# <font color=green> PYTHON PARA DATA SCIENCE - PANDAS
---

# <font color=green> 1. INTRODUÇÃO AO PYTHON
---

# 1.1 Introdução

> Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares. 
>
> Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assundo é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado.

# 1.2 Instalação e ambiente de desenvolvimento

### Instalação Local

### https://www.python.org/downloads/
### ou
### https://www.anaconda.com/distribution/

### Google Colaboratory

### https://colab.research.google.com

### Verificando versão
"""

!python -V

"""# 1.3 Trabalhando com dados"""

import pandas as pd

#Para poder escolher a quantidade de linhas que deve aparecer no data set
#pd.set_option('display.max_rows', 1000)

#Para poder escolher a quantidade de colunas que deve aparecer no data set
#pd.set_option('display.max_columns', 1000)

dataset = pd.read_csv('db.csv', sep = ';')

dataset

dataset.dtypes

#Conjunto de estatística descritiva de algum objeto do Dataset
dataset[['Quilometragem', 'Valor']].describe()

dataset.info()



"""# <font color=green> 2. TRABALHANDO COM TUPLAS
---

# 2.1 Criando tuplas

Tuplas são sequências imutáveis que são utilizadas para armazenar coleções de itens, geralmente heterogêneos. Podem ser construídas de várias formas:
```
- Utilizando um par de parênteses: ( )
- Utilizando uma vírgula à direita: x,
- Utilizando um par de parênteses com itens separados por vírgulas: ( x, y, z )
- Utilizando: tuple() ou tuple(iterador)
```
"""

()

1,2,3

nome = 'Passat'
valor = 153000
(nome,valor)

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
nomes_carros

type(nomes_carros)

"""# 2.2 Seleções em tuplas"""

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

nomes_carros[0]

nomes_carros[1]

nomes_carros[-1]

nomes_carros[1:3]

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
nomes_carros

nomes_carros[-1]

nomes_carros[-1][1]

"""# 2.3 Iterando em tuplas"""

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

for item in nomes_carros:
  print(item)

"""### Desempacotamento de tuplas"""

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

carro_1,carro_2,carro_3,carro_4 = nomes_carros

carro_1

carro_2

carro_3

carro_4

_,A,_,B = nomes_carros

A

B

_,C,*_ = nomes_carros

C

"""## *zip()*

https://docs.python.org/3.6/library/functions.html#zip
"""

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
carros

valores = [88078.64, 106161.94, 72832.16, 124549.07]
valores

list(zip(carros, valores))

for item in zip(carros, valores):
  print(item)

for carro, valor in zip(carros, valores):
  print(carro, valor)

for carro, valor in zip(carros, valores):
  if valor > 100000:
    print(carro)

"""# <font color=green> 3. TRABALHANDO COM DICIONÁRIOS
---

# 3.1 Criando dicionários

Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices (números inteiros) para acessar os valores.

Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento. Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido como chave (*key*) e o segundo como valor (*value*).

```
dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n}
```

https://docs.python.org/3.6/library/stdtypes.html#typesmapping
"""



carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros

valores = [88078.64, 106161.94, 72832.16]
valores









"""### Criando dicionários com *zip()*"""





"""# 3.2 Operações com dicionários

## *dict[ key ]*

Retorna o valor correspondente à chave (*key*) no dicionário.
"""



"""## *key in dict*

Retorna **True** se a chave (*key*) for encontrada no dicionário.
"""







"""## *len(dict)*

Retorna o número de itens do dicionário.
"""



"""## *dict[ key ] = value*

Inclui um item ao dicionário.
"""





"""## *del dict[ key ]*

Remove o item de chave (*key*) do dicionário.
"""





"""# 3.3 Métodos de dicionários

## *dict.update()*

Atualiza o dicionário.
"""





"""## *dict.copy()*

Cria uma cópia do dicionário.
"""









"""## *dict.pop(key[, default ])*

Se a chave for encontrada no dicionário, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como *default* é retornado. Se o valor *default* não for fornecido e a chave não for encontrada no dicionário um erro será gerado.
"""



















"""## *dict.clear()*

Remove todos os itens do dicionário.
"""





"""# 3.4 Iterando em dicionários

## *dict.keys()*

Retorna uma lista contendo as chaves (*keys*) do dicionário.
"""





"""## *dict.values()*

Retorna uma lista com todos os valores (*values*) do dicionário.
"""



"""## *dict.items()*

Retorna uma lista contendo uma tupla para cada par chave-valor (*key-value*) do dicionário.
"""









"""# <font color=green> 4. FUNÇÕES E PACOTES
---
    
Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado.

# 4.1 Built-in function

A linguagem Python possui várias funções integradas que estão sempre acessíveis. Algumas já utilizamos em nosso treinamento: type(), print(), zip(), len(), set() etc.

https://docs.python.org/3.6/library/functions.html
"""

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados













"""# 4.2 Definindo funções sem e com parâmetros

### Funções sem parâmetros

#### Formato padrão

```
def <nome>():
    <instruções>
```
"""





"""### Funções com parâmetros

#### Formato padrão

```
def <nome>(<param_1>, <param_2>, ..., <param_n>):
    <instruções>
```
"""















"""# 4.3 Definindo funções que retornam valores

### Funções que retornam um valor

#### Formato padrão

```
def <nome>(<param_1>, <param_2>, ..., <param_n>):
    <instruções>
    return <resultado>
```
"""









"""### Funções que retornam mais de um valor

#### Formato padrão

```
def <nome>(<param_1>, <param_2>, ..., <param_n>):
    <instruções>
    return (<resultado_1>, <resultado_2>, ..., <resultado_n>)
```
"""











"""# <font color=green> 5. PANDAS BÁSICO
---

**versão: 0.25.2**
  
Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.


## Estruturas de Dados

### Series

Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de **index**. A forma básica de criação de uma Series é a seguinte:


```
    s = pd.Series(dados, index = index)
```

O argumento *dados* pode ser um dicionário, uma lista, um array Numpy ou uma constante.

### DataFrames

DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.


```
    df = pd.DataFrame(dados, index = index, columns = columns)
```

O argumento *dados* pode ser um dicionário, uma lista, um array Numpy, uma Series e outro DataFrame.

**Documentação:** https://pandas.pydata.org/pandas-docs/version/0.25/

# 5.1 Estruturas de dados
"""



"""### Criando uma Series a partir de uma lista"""





"""### Criando um DataFrame a partir de uma lista de dicionários"""

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]







"""### Criando um DataFrame a partir de um dicionário"""

dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}





"""### Criando um DataFrame a partir de uma arquivo externo"""





"""# 5.2 Seleções com DataFrames

### Selecionando colunas
"""









"""### Selecionando linhas - [ i : j ] 

<font color=red>**Observação:**</font> A indexação tem origem no zero e nos fatiamentos (*slices*) a linha com índice i é **incluída** e a linha com índice j **não é incluída** no resultado.
"""



"""### Utilizando .loc para seleções

<font color=red>**Observação:**</font> Seleciona um grupo de linhas e colunas segundo os rótulos ou uma matriz booleana.
"""









"""### Utilizando .iloc para seleções

<font color=red>**Observação:**</font> Seleciona com base nos índices, ou seja, se baseia na posição das informações.
"""











"""# 5.3 Queries com DataFrames"""











"""### Utilizando o método query"""



"""# 5.4 Iterando com DataFrames"""





"""# 5.5 Tratamento de dados"""























