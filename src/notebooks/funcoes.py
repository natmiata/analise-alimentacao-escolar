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
    plt.xticks(rotation=90)

    return plt.show


def plot_hist(df, coluna, coluna_media, titulo, xlabel):
    
    """
    Objetivo: Plotar um histograma.
    Input - df = dataframe
            coluna = nome da coluna a ser plotada.
            coluna_media = nome da coluna a ser plotada no valor da média.
            titulo = titulo do gráfico
            xlabel = texto a ser exibido no eixo x.
    Output - Histograma.
    """

    plt.figure(figsize=(12,8))
    plt.hist(df[coluna], bins=50, alpha=0.5)
    plt.axvline(df[coluna_media].mean(), color='#151B54', linestyle='dashdot', linewidth=2, label='Média')
    plt.xlabel(xlabel, size=16)
    plt.ylabel("Frequência", size=16)
    plt.title(titulo, size=20)
    plt.legend(loc='upper right')
    plt.tick_params(axis="both", which="major", labelsize=12)
    
    return plt.show


def plot_bar_h(df, coluna, titulo, ylabel):

    """
    Objetivo: Plotar um gráfico de barras na horizontal.
    Input - df = dataframe
            coluna = nome da coluna a ser plotada
            titulo = titulo do gráfico
            ylabel = texto a ser exibido no eixo x.
    Output - Plot em barras.
    """

    plt.figure(figsize=(15, 6))
    df[coluna].value_counts(normalize=True).iloc[:10].plot.barh(color="#151B54")
    plt.title(titulo, size=20)
    plt.ylabel(ylabel, size=16)
    plt.xlabel('Frequência', size=16)
    plt.tick_params(axis="both", which="major", labelsize=14)
    plt.xticks(rotation=45)

    return plt.show