import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

# Carregar os dados
df_imoveis = pd.read_csv('base-de-dados.csv')

# Limpar dados nulos na coluna 'preco' e em colunas essenciais
df_imoveis = df_imoveis.dropna(subset=['preco', 'bairro', 'quartos', 'data_publicacao'])

# Converter coluna 'data_publicacao' para tipo datetime
df_imoveis['data_publicacao'] = pd.to_datetime(df_imoveis['data_publicacao'])

# Calcular idade do imóvel em anos (a partir da data de publicação)
df_imoveis['idade_imovel'] = datetime.now().year - df_imoveis['data_publicacao'].dt.year

# Definir variáveis de entrada (features) e saída (target)
X = df_imoveis[['bairro', 'quartos', 'idade_imovel']]
y = df_imoveis['preco']

# Converter variáveis categóricas em variáveis dummy
X = pd.get_dummies(X, columns=['bairro'])

# Dividir o conjunto de dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Otimização dos hiperparâmetros usando GridSearchCV com Ridge Regression
parameters = {'alpha': [0.1, 1, 10, 100]}
ridge = Ridge()
clf = GridSearchCV(ridge, parameters, cv=5)
clf.fit(X_train, y_train)

# Melhor modelo após a otimização
best_model = clf.best_estimator_

# Avaliação do modelo usando validação cruzada
cv_scores = cross_val_score(best_model, X, y, cv=5)

# Treinar o modelo otimizado no conjunto de treinamento completo
best_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = best_model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMelhor Modelo: {best_model}")
print(f"\nMean Squared Error: {mse}")
print(f"R-squared: {r2}")
print(f"\nCross-Validation Scores: {cv_scores}")
print(f"Mean CV Score: {cv_scores.mean()}")

# Exibir previsões e valores reais de forma detalhada
df_results = pd.DataFrame({'Atual': y_test, 'Sugerido': y_pred})
df_results = df_results.reset_index(drop=True)  # Resetar índice para alinhamento
df_detalhado = pd.concat([df_imoveis.iloc[y_test.index].reset_index(drop=True), df_results], axis=1)

# Configuração para exibir todas as linhas do DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print("\nResultados detalhados:")
print(df_detalhado)
