#!/bin/sh

# Get current date & time
date=$(date +'%Y%m%d')
time=$(date +'%H%M%S')
echo "$date $time"

# Download the latest csv of stock price
python /home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/Taiwan_Stocks/update_taiwan_stock.py

# Make prediction
python /home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/all_stock_4value_together.pyi

# Copy TOMORROW_PRICE.csv to /home/marktsao/stock_website
cp /home/marktsao/DLpractice/Stock_Prices_Prediction_LSTM/TOMORROW_PRICE.csv /home/marktsao/stock_website/TOMORROW_PRICE.csv

# Push to github 
cd /home/marktsao/stock_website/
/usr/bin/git add -A
/usr/bin/git commit -m "$date auto update"
/usr/bin/git push origin master
