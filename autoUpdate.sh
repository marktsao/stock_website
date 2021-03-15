#!/bin/bash

# Get current date & time
date=$(date +'%Y%m%d')
time=$(date +'%H%M%S')
echo "$date $time"

token=""

if [$1=="public"]
then
    token="Oh4jBjR5YQAvw2GUmAZByamh25dKIgY3HMshDACzhLr" # public
else
    token="gZd0yMvonRUdlrR9LSquHCIKGGau7hjjADlzLxOmJ3W" # private
fi

# curl -X POST -H "Authorization: Bearer $token" -d "message=$date 訓練開始" https://notify-api.line.me/api/notify
# curl -X POST -H "Authorization: Bearer gZd0yMvonRUdlrR9LSquHCIKGGau7hjjADlzLxOmJ3W" -d "message=$date 訓練開始" https://notify-api.line.me/api/notify # private
# curl -X POST -H "Authorization: Bearer Oh4jBjR5YQAvw2GUmAZByamh25dKIgY3HMshDACzhLr" -d "message=$date 訓練開始" https://notify-api.line.me/api/notify # public

source /home/marktsao/anaconda3/etc/profile.d/conda.sh
conda activate myenv

# Download the latest csv of stock price
cd /home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks
python update_taiwan_stock.py

# Make prediction
cd /home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM
python all_stock_4value_together.py

# Copy TOMORROW_PRICE.csv to /home/marktsao/stock_website
cp /home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/TOMORROW_PRICE.csv /home/marktsao/stock_website

# Push to github 
cd /home/marktsao/stock_website/
/usr/bin/git add -A
/usr/bin/git commit -m "$date auto update"
/usr/bin/git push origin master

# curl -X POST -H "Authorization: Bearer $token" -d "message=$date 訓練完成
# 查看結果：https://marktsao.github.io/stock_website/" https://notify-api.line.me/api/notify
# curl -X POST -H "Authorization: Bearer gZd0yMvonRUdlrR9LSquHCIKGGau7hjjADlzLxOmJ3W" -d "message=$date 訓練完成
# 查看結果：https://marktsao.github.io/stock_website/" https://notify-api.line.me/api/notify # private
curl -X POST -H "Authorization: Bearer Oh4jBjR5YQAvw2GUmAZByamh25dKIgY3HMshDACzhLr" -d "message=$date 訓練完成
查看結果：https://marktsao.github.io/stock_website/" https://notify-api.line.me/api/notify # public