import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.api import OLS


#Pegando o template com as informações no modelo de csv, e transformando em DF
df = pd.open_csv('template_df_unimovel.csv')


class RenderGraphic:
    
    def get_columns(x, y, df):
        sns.scatterplot(x=x, y=y, data=df)

        return plt.show()


#classe para organizar os métodos responsáveis pelas filtragens. 
class FilterDf:

    def _filter_by_city(df, value):
        filtered_df = df[df['Cidade'] == value]
        if filtered_df.empty:
            print('sem resultados')
        else: 
            print(f"Foram encontrados {len(filtered_df)} resultados e a média de aluguel dessa cidade é de R$ {filtered_df['Aluguel'].mean()}")

        return filtered_df 

    def _filter_by_owner(df, value):
        filtered_df = df[df['Nome do proprietario'] == value]
        if filtered_df.empty:
            print('sem resultados')
        else:
            print(f"Foram encontrados {len(filtered_df)} resultados e a média de aluguel desse proprietário é de R$ {filtered_df['Aluguel'].mean()}")

        return filtered_df

    def _filter_by_rooms(df, value):
        filtered_df = df[df['Quartos'] == value]
        if filtered_df.empty:
            print('sem resultados')
        else:
            print(f"Foram encontrados {len(filtered_df)} resultados e a média de aluguel dessa quantidade de quartos é de R$ {filtered_df['Aluguel'].mean()}")

        return filtered_df

    def _filter_by_type_of_property(df, value):
        filtered_df = df[df['Tipo Propriedade'] == value]
        if filtered_df.empty:
            print('sem resultados')
        else:
            print(f"Foram encontrados {len(filtered_df)} resultados e a média de aluguel desse tipo de propriedade é de R$ {filtered_df['Aluguel'].mean()}")

        return filtered_df
    
    def _filter_by_price(df, value):
        filtered_df = df[df['Aluguel'] == value]
        if filtered_df.empty:
            print('sem resultados')
        else:
            print(f"Foram encontrados {len(filtered_df)} resultados.")

        return filtered_df


#classe onde armazenará as funções para análises estatisticas.
class StatisticsTools:
    def get_ols(df):
        y = df['Aluguel']
        x = df['Quartos']

        model = OLS(y, x)
        results = model.fit()
        return results.summary()


#utilizando a filtragem
#Guardando numa variável o DF filtrado, para assim usar nas comparações com gráficos. 

filtrado_cidade = FilterDf._filter_by_city(df=df, value="São Paulo")

#Utilizando a vizualição por gráfico

grafico = RenderGraphic.get_columns(x='Aluguel', y='Quartos', df=filtrado_cidade)

#dentro da variável gráfico fica armazenado a visualização através do método show() 


#criando um output de uma analise a partir do modelo OLS
model_ols = StatisticsTools.get_ols(df=filtrado_cidade)

