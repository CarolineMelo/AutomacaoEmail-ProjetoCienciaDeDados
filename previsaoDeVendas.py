import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

tabela = pd.read_csv(r'C:\Users\carlo\OneDrive\Documents\carol\cursos\Python Impressionador\Aula 4\advertising.csv')
# print(tabela.info())

#correlação -1 ->
# print(tabela.corr())

# criar um grafico
sns.heatmap(tabela.corr(), cmap='Greens', annot=True)
# #exibe o gráfico
plt.show()
y = tabela['Vendas'] # y é sempre o que eu quero prever
x = tabela[['TV','Radio','Jornal']]

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.3)

# importar a inteligencia artificial
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# criar a inteligencia artificial
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treinar a inteligencia artificial
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

#Teste de AI e Avaliação do Melhor Modelo : usar o r2 -> diz que o % que o nosso modelo consegue explicar o que acontece
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score
print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))

#Visualização Gráfica das Previsões
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsao Arvore Decisao'] = previsao_arvoredecisao
tabela_auxiliar['Previsao RegressaoLonear'] = previsao_arvoredecisao

sns.lineplot(data= tabela_auxiliar)
plt.show()

#Como fazer uma previsão
nova_tabela = pd.read_csv(r'C:\Users\carlo\OneDrive\Documents\carol\cursos\Python Impressionador\Aula 4\novos.csv')
print(nova_tabela)
previsao =modelo_arvoredecisao.predict(nova_tabela)
print(previsao)
