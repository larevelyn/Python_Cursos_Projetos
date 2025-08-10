# %%
# Importando o arquivo de teste
import pandas as pd
teste = pd.read_csv('arquivos/casas_teste.csv')

# %%
# Fazendo o load do modelo
from joblib import load
reg = load('modelo/regressao.joblib')

# %%
# Fazendo a previsão
teste = teste.drop('Unnamed: 0', axis=1)
X_teste = teste.drop('MedHouseVal', axis=1)


# %%
# Exportando esse arquivo
previsao = reg.predict(X_teste)
X_teste['previsao'] = previsao

X_teste.to_excel('saida_modelo/previsoes_modelo.xlsx')

# %%



