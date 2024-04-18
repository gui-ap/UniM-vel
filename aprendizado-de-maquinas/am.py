import pandas as pd
from datetime import datetime

# Para instalar a biblioteca abaixo pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# Criar DataFrame a partir dos dados em uma planilha csv
df_imoveis = pd.read_csv('base-de-dados.csv')

# Limpar dados nulos
df_imoveis = df_imoveis.dropna()

# Converter coluna 'data_publicacao' para tipo datetime
df_imoveis['data_publicacao'] = pd.to_datetime(df_imoveis['data_publicacao'])

# Calcular idade do imóvel em anos (a partir da data de publicação)
df_imoveis['idade_imovel'] = datetime.now().year - df_imoveis['data_publicacao'].dt.year

print(df_imoveis)

# Definir variáveis de entrada (features) e saída (target)
X = df_imoveis[['bairro', 'quartos', 'preco', 'idade_imovel']]
y = df_imoveis['tipo']

# Converter variáveis categóricas em variáveis dummy
X = pd.get_dummies(X)

# Dividir o conjunto de dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de classificação
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Obter todas as classes conhecidas
all_classes = df_imoveis['tipo'].unique()

# Calcular a matriz de confusão com todas as classes conhecidas
cm = confusion_matrix(y_test, y_pred, labels=all_classes)

print("\nMatriz de Confusão:")
print(cm)