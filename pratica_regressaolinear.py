# -*- coding: utf-8 -*-
"""pratica_regressaolinear.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C_J1qW3lnFU-KHgSbvWLhqQNKlsd61S5
"""

#importando as Bibliotecas
import pandas as pd #Trabalhar com tabelas e importação de Arquivos utilizados
import plotly.express as px #biblioteca responsável por criar  Gráficos Dinamicos
import seaborn as sns #biblioteca para Graficos
import numpy as np # funções matemáticas  de alto nivel

"""#Abrindo o Arquivo contendo os dados """

base_custo_diario = pd.read_csv('base_custo_diaria.csv',sep=';')

#visualizando a base de dados
base_custo_diario.head

# algumas estátisticas de Base de dados 
base_custo_diario.describe()

"""#criando as Variáveis que serão utilizadas no modelo"""

X_custo_diario = base_custo_diario.iloc[:,0].values #buscamos todos os valores da primeira coluna e convertemos para formato de array
# o comando iloc permite selecionar um grupo de registros o ":" significa que estamos selecionando todos os registros e  0 da primeira coluna
X_custo_diario

#Criando a variável dependente que queremos predizer
y_custo_diario = base_custo_diario.iloc[:,1].values
y_custo_diario

np.corrcoef(X_custo_diario, y_custo_diario) # mostra uma matriz

"""#Correlação 
## correlação positiva: quando ocorre de 2 variaveis ou crescerem ou decrescerem juntas
## correlação negativa , as duas são ligadas porem inversamente
##não correlacionada: uma não interfere na outra
"""

correlation = base_custo_diario.corr()
#plot da matriz de correlação
plot = sns.heatmap(correlation, annot = True, linewidths=.3)
plot

"""#Tratando os Dados  para o modelo"""

#visualizar o formato da Váriavel
X_custo_diario.shape

#vizualizando a variavel
X_custo_diario # o resultado mostra que temos um array com apenas uma coluna/dimensão. NO entando,precisamos ter uma matriz com  2 colunas

X_custo_diario = X_custo_diario.reshape(-1,1)
X_custo_diario

#Agora nós temos uma matriz com 2 colunas. 10 linhas e 1 coluna
X_custo_diario.shape

"""#aplicando o algoritimo para a machine de Regressão"""

from sklearn.linear_model import LinearRegression
#Cria um objeto do tipo Regreessão linear
previsao_custo_diario = LinearRegression()

type(previsao_custo_diario)

"""#Realizando o Treinamento do Modo"""

previsao_custo_diario.fit(X_custo_diario,y_custo_diario)

#verificando a interceptação
previsao_custo_diario.intercept_

#Verificando o coeficiente linear da  reta
previsao_custo_diario.coef_

previsao_precos = previsao_custo_diario.predict(X_custo_diario)#baseado nos valores de n de pessoas vamos estimar/prever  o custodo imovel alugado

#visualizando as previsoes para cada numero de pessoas
previsao_precos

"""#Visualisando  no grafico as disposições dos dados

##para vizualizar dados no grafico eles tem que ser vetor para isso usamos o comando  ravel()
"""

#verificando o tipo da variável X_custo diaria
X_custo_diario

X_custo_diario.ravel()# transforma em um vetor

y_custo_diario

grafico = px.scatter(x = X_custo_diario.ravel(),y = y_custo_diario)
grafico.show()

grafico = px.scatter(x = X_custo_diario.ravel(), y = y_custo_diario)
grafico.add_scatter(x= X_custo_diario.ravel(),y = previsao_precos, name='previsões'  )
grafico.show()

#verificando os valores baseados numa determinada quantidade de pessoas
qtd_pessoas = 4
previsao_custo_diario.intercept_ + previsao_custo_diario.coef_  * qtd_pessoas

qtd_pessoas = 8
previsao_custo_diario.intercept_ + previsao_custo_diario.coef_  * qtd_pessoas

#verificando de modo direto
previsao_custo_diario.predict([[8]])

#indica a quantidade de algoritimo(quanto mais proximo de 1 ,melhor a qualidade do modelo)
previsao_custo_diario.score(X_custo_diario, y_custo_diario)

#vizualizando os  erros de modelo
from sklearn.metrics import mean_squared_error, mean_absolute_error
MSE= mean_squared_error(y_custo_diario, previsao_precos)

MSE

#calculando MAE
mean_absolute_error(y_custo_diario,previsao_precos)

#calculando o   RMSE
np.sqrt(MSE)