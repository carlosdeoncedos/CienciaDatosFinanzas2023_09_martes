import pandas as pd
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