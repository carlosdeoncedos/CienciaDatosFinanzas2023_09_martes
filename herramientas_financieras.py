import pandas as pd
import numpy as np
import datetime



def precios(accion, fecha1, fecha2):
    fecha1_ = datetime.datetime.strptime(fecha1, '%Y-%m-%d').strftime('%s')
    fecha2_ = datetime.datetime.strptime(fecha2, '%Y-%m-%d').strftime('%s')
    
    url_ = f'https://query1.finance.yahoo.com/v7/finance/download/{accion}?period1={fecha1_}&period2={fecha2_}&interval=1d&events=history&includeAdjustedClose=true'
    # print(url_)
    df_ = pd.read_csv(url_)
    df_['Date'] = pd.to_datetime(df_['Date'])
    df_.set_index('Date', inplace=True)
    
    
    return df_

def sumar(a, b):
    sumatoria = a + b
    
    return sumatoria








"""
Funciones para generar las gráficas de la sesión 7
"""

from matplotlib.patches import FancyArrow
from matplotlib.patches import Circle
import matplotlib.pyplot as plt

def mezcla_colores(peso, color1, color2):
    # Descomponemos los colores en sus componentes R, G, B
    componente1 = tuple(int(color1[i:i+2], 16)/255 for i in (0, 2, 4))
    componente2 = tuple(int(color2[i:i+2], 16)/255 for i in (0, 2, 4))

    # Calculamos la media ponderada de las componentes
    color_mezclado = [(peso*componente1[i] + (1-peso)*componente2[i]) for i in range(3)]
    
    # Convertimos el color mezclado a formato hexadecimal
    return '#{:02x}{:02x}{:02x}'.format(*(int(c*255) for c in color_mezclado))


def fig_2activos(df_2activos):
    fig, ax = plt.subplots(figsize=(12,6))
    ax.set_title('Gráfica Activos Rojo y Azul')

    plt.xlabel('Riesgo', fontsize = 10)
    plt.ylabel('Retorno', fontsize = 10)
    # Limitar los ticks a unicamente los valores de ret y sigma en df_2activos:
    plt.xticks(df_2activos.loc['sigma'])
    plt.yticks(df_2activos.loc['ret'])

    #lista de colores 
    list_color=['red', 'blue']
    i = 0

    """
    For loop para imprimir la ubicación de cada activo, asi como las líneas verticales y horizontales.
    Para que las líneas sobrepasaran el punto le sume + .01 a la longitud de la líneas
    Poner atención como cambia el color de acuerdo al contador 'i':
    """
    for activo in df_2activos.columns:
        ax.hlines(df_2activos[activo].loc['ret'], 0, df_2activos[activo].loc['sigma'] + .01, lw=.8, ls='--', color=list_color[i])
        ax.vlines(df_2activos[activo].loc['sigma'], 0, df_2activos[activo].loc['ret'] + 0.01, lw=.8, ls='--', color=list_color[i])
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=1500, label= activo, color=list_color[i], alpha=.15)
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=300, label= activo, color=list_color[i])
        i += 1

    #Quitar las líneas del perímetro de la gráfica   
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    #Agregar flechas para el eje de las X's y Y's
    arrow_x = FancyArrow(0, 0, .35, 0, head_width=0.005, head_length=0.006, fc='gray', ec='gray', linewidth=0.1)
    arrow_y = FancyArrow(0, 0, 0, 0.15, head_width=0.005, head_length=0.006, fc='gray', ec='gray', linewidth=0.1)
    ax.add_patch(arrow_x)
    ax.add_patch(arrow_y);
    
    
def fig_pregunta(df_2activos):
    fig, ax = plt.subplots(figsize=(12,6))
    ax.set_title=('sdsd')

    plt.xlabel('Riesgo', fontsize = 14)
    plt.ylabel('Retorno', fontsize = 14)
    # Limitar los ticks a unicamente los valores de ret y sigma en df_2activos:
    plt.xticks(df_2activos.loc['sigma'])
    plt.yticks(df_2activos.loc['ret'])

    #lista de colores 
    list_color=['red', 'blue']
    i = 0

    """
    For loop para imprimir la ubicación de cada activo, asi como las líneas verticales y horizontales.
    Para que las líneas sobrepasaran el punto le sume + .01 a la longitud de la líneas
    Poner atención como cambia el color de acuerdo al contador 'i':
    """
    for activo in df_2activos.columns:
        ax.hlines(df_2activos[activo].loc['ret'], 0, df_2activos[activo].loc['sigma'] + .01, lw=.8, ls='--', color=list_color[i])
        ax.vlines(df_2activos[activo].loc['sigma'], 0, df_2activos[activo].loc['ret'] + 0.01, lw=.8, ls='--', color=list_color[i])
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=1500, label= activo, color=list_color[i], alpha=.15)
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=300, label= activo, color=list_color[i])
        i += 1

    #Quitar las líneas del perímetro de la gráfica   
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    #Agregar flechas para el eje de las X's y Y's
    arrow_x = FancyArrow(0, 0, .35, 0, head_width=0.005, head_length=0.006, fc='gray', ec='gray', linewidth=0.1)
    arrow_y = FancyArrow(0, 0, 0, 0.15, head_width=0.005, head_length=0.006, fc='gray', ec='gray', linewidth=0.1)
    ax.add_patch(arrow_x)
    ax.add_patch(arrow_y)

    ax.scatter(.25, .08, marker = '.', s=1500, label= activo, color='green', alpha=.15)
    ax.scatter(.25, .08, marker = '.', s=300, label= activo, color='green')
    ax.set_xticks([.2,.25,.3])
    ax.set_yticks([.04, .08, .12])
    ax.plot([.2 , .3], [.04, .12], lw=.8, ls='--', color='green')
    ax.hlines(.08, 0, .25 + .01, lw=.8, ls='--', color='green')
    ax.vlines(.25, 0, .08 + 0.01, lw=.8, ls='--', color='green')
    
    
    '''
En esta función utilizo dos maneras diferentes de ir cambiando los colores de las figuras:
1. De manera vectorizada con pandas
2. A través de un for loop y de una variable incremental
'''

def fig_portafolio(df_2activos, rho):

    df_portafolio2activos = portafolio(df_2activos, rho)
    df_portafolio2activos['colores'] = df_portafolio2activos.apply(lambda row: mezcla_colores(row['w_rojo'], 'ff0000', '0018ff'), axis=1)

    fig, ax = plt.subplots(figsize=(12,6))
    ax.set_title('Portafolios con diferentes proporciones de pesos en los activos "Azul" y "Rojo"; ' + r'$\rho$' + f'={rho}')

    plt.yticks([.04,.12])

    ax.scatter(df_portafolio2activos['sigma'].iloc[1:-1], df_portafolio2activos['retorno'].iloc[1:-1], color=df_portafolio2activos['colores'].iloc[1:-1], s=100)

    colores=['#ff0000', '#0018ff']

    i = 0
    for activo in df_2activos.columns:
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=1500, label= activo, color=colores[i], alpha=.15)
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=300, label= activo, color=colores[i])
        i += 1

    ax.set_xlabel('sigma')
    ax.set_ylabel('retorno')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False);
    

def fig_port_dif_correlacion(df_2activos):
    rho=.1
    list_color = ['red', 'blue']

    df_portafolio2activos = portafolio(df_2activos, rho)
    list_rho = np.arange(0, 1.01, .1)
    fig, ax = plt.subplots(figsize=(12,6))

    for rho in list_rho:
        df_portafolio2activos = portafolio(df_2activos, rho, False)
        ax.plot(df_portafolio2activos['sigma'], df_portafolio2activos['retorno'], label=f'rho={rho:.1f}')

    i = 0
    for activo in df_2activos.columns:
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=1500, color=list_color[i], alpha=.15)
        plt.scatter(df_2activos[activo].loc['sigma'], df_2activos[activo].loc['ret'], marker = '.', s=300, color=list_color[i],)
        i += 1

    ax.set_xlabel('sigma')
    ax.set_ylabel('retorno')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.legend(frameon=False);
    
    
def portafolio(df_2activos, r, pocos=True):
    """
    Cálculo vectorizado de los pesos, retornos y volatilidad
    de un portafolio de 2 activos.
    requiere un dataframe con los retornos y volatilidades
    de cada uno de los activos y su correlación
    """
    if pocos == True:
        a = np.arange(0.0, 1.1, .1)
    elif pocos == False:
        a = np.arange(0.0, 1.01, .01)
    df_ = pd.DataFrame()
    df_['w_rojo'] = a
    df_['w_azul'] = 1 - df_['w_rojo']
    df_['retorno'] = (
        df_2activos['rojo'].loc['ret'] * df_['w_rojo'] +
        df_2activos['azul'].loc['ret'] * df_['w_azul']
    )

    df_['sigma'] = (
        (df_2activos['rojo'].loc['sigma']**2)*(df_['w_rojo']**2) +
        (df_2activos['azul'].loc['sigma']**2)*(df_['w_azul']**2) +
        (2 * 
         df_['w_rojo'] * 
         df_['w_azul'] * 
         df_2activos['rojo'].loc['sigma'] * 
         df_2activos['azul'].loc['sigma'] *
         r
        ) 
    )**.5
    
    return df_