#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:59:57 2021

@author: marktsao
"""

import requests
from io import StringIO
import pandas as pd
import numpy as np
from datetime import datetime as dt
today = dt.now()
datestr = today.strftime('%Y%m%d')
#datestr = '20210310'
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '})
     for i in r.text.split('\n') 
     if len(i.split('",')) == 17 and i[0] != '='])), header=0)

df.columns = ["number","name","vol","vol2","price","open","high","low","close","nan2","nan3","nan4","nan5","nan6","nan7","nan8","nan9"]

#7 stocks I intersting in 
scores = {"number":[],"name":[],"vol":[],"vol2":[],"price":[],"open":[],"high":[],"low":[],"close":[],"nan2":[],"nan3":[],"nan4":[],"nan5":[],"nan6":[],"nan7":[],"nan8":[],"nan9":[]}
stocks_7 = pd.DataFrame.from_dict(scores)
for i in range(len(df)):
    if df.number[i] == '2317':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    elif df.number[i] == '2327':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    elif df.number[i] == '2330':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    elif df.number[i] == '2379':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    elif df.number[i] == '2454':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    elif df.number[i] == '3034':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    elif df.number[i] == '3661':
        stocks_7 = stocks_7.append(df[i:i+1],ignore_index=True)
    else:
        continue
stocks_7_4_value = stocks_7[["number","open","close","high","low"]]     
stocks_7_4_value["date"]=[datestr,datestr,datestr,datestr,datestr,datestr,datestr]
stocks_7_4_value["volu"]=[0,0,0,0,0,0,0]
stocks_7_4_value["e%"]=[0,0,0,0,0,0,0]

stocks_7_4_value_2317 = stocks_7_4_value[0:1].reindex(columns=['date','close','open','high','low','volu','e%'])
stocks_7_4_value_2327 = stocks_7_4_value[1:2].reindex(columns=['date','close','open','high','low','volu','e%'])
stocks_7_4_value_2330 = stocks_7_4_value[2:3].reindex(columns=['date','close','open','high','low','volu','e%'])
stocks_7_4_value_2379 = stocks_7_4_value[3:4].reindex(columns=['date','close','open','high','low','volu','e%'])
stocks_7_4_value_2454 = stocks_7_4_value[4:5].reindex(columns=['date','close','open','high','low','volu','e%'])
stocks_7_4_value_3034 = stocks_7_4_value[5:6].reindex(columns=['date','close','open','high','low','volu','e%'])
stocks_7_4_value_3661 = stocks_7_4_value[6:7].reindex(columns=['date','close','open','high','low','volu','e%'])
"""
2317
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/2317.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_2317,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='2317.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()
"""
2327
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/2327.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_2327,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='2327.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()
"""
2330
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/2330.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_2330,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='2330.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()
"""
2379
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/2379.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_2379,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='2379.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()
"""
2454
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/2454.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_2454,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='2454.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()
"""
3034
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/3034.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_3034,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='3034.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()
"""
3661
"""
dataset_path = "/home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/3661.csv"
df = pd.read_csv(dataset_path)
df_3 = df.copy()
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
df = df.append(stocks_7_4_value_3661,ignore_index=True)
for i in range(len(df)):
    df_3.date[i] = 0
    df_3.date[i] = df.date[len(df)-1-i]
    df_3.close[i] = 0
    df_3.close[i] = df.close[len(df)-1-i]
    df_3.open[i] = 0
    df_3.open[i] = df.open[len(df)-1-i]
    df_3.high[i] = 0
    df_3.high[i] = df.high[len(df)-1-i]
    df_3.low[i] = 0
    df_3.low[i] = df.low[len(df)-1-i]
df = df_3
def OutputCSV():       
    Result ='3661.csv'
    df_SAMPLE = pd.DataFrame.from_dict( df_3 )
    df_SAMPLE.to_csv( Result  , index=False )  
    print( ''+Result )  
OutputCSV()