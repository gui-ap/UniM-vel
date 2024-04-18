import pandas as pd
from datetime import datetime

# Criar dados de exemplo (pode substituir por seus próprios dados reais)
dados_imoveis = {
    'id': [1, 2, 3, 4, 5],
    'tipo': ['Casa', 'Apartamento', 'Casa', 'Apartamento', 'Terreno'],
    'bairro': ['Centro', 'Zona Sul', 'Zona Norte', 'Centro', 'Zona Oeste'],
    'quartos': [3, 2, 4, 1, 0],
    'preco': [300000, 200000, 400000, 150000, 80000],
    'data_publicacao': ['2022-01-01', '2022-02-15', '2022-03-10', '2022-04-20', '2022-05-05']
}

# Criar DataFrame a partir dos dados
df_imoveis = pd.DataFrame(dados_imoveis)

# Converter coluna 'data_publicacao' para tipo datetime
df_imoveis['data_publicacao'] = pd.to_datetime(df_imoveis['data_publicacao'])

# Calcular idade do imóvel em anos (a partir da data de publicação)
df_imoveis['idade_imovel'] = datetime.now().year - df_imoveis['data_publicacao'].dt.year

print(df_imoveis)