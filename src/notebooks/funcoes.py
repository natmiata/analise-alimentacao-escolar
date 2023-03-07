import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)


def plot_bar(df, coluna_x, coluna_y, titulo, xlabel):

    """
    Objetivo: Plotar um gráfico de barras.
    Input - df = dataframe
            coluna_x = nome da coluna a ser plotada no eixo x
            coluna_y = nome da coluna a ser plotada no eixo y
            titulo = titulo do gráfico
            xlabel = texto a ser exibido no eixo x.
    Output - Plot em barras.
    """

    df.plot(x=coluna_x, y=coluna_y, kind='bar', color="#151B54", figsize=(18,7))
    plt.title(titulo, size=22)
    plt.ylabel("Frequência", size=18)
    plt.xlabel(xlabel, size=18)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.xticks(rotation=45)

    return plt.show
