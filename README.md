# Bitcoin-Predictor
# Bitcoin Price Prediction with Linear Regression

This project fetches historical Bitcoin prices from Yahoo Finance, uses linear regression to predict the next day's price, and returns a prediction in USD.

## Table of Contents
- [Description]
- [Installation]
- [Usage](
- [API]
- [Algorithm Explanation]
- [Dependencies]


## Description

This Python script utilizes Yahoo Finance to retrieve the last 10 days of Bitcoin (BTC-USD) prices, calculates the average price based on the high and low prices, and then uses linear regression to predict the price for the next day.

## Installation

To set up the project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/amir-khazaee/Bitcoin-Predictor.git
   cd Bitcoin-Predictor
## Usage
To run the script, simply execute the Python file in your terminal:
python main.py

## API
The script fetches data from Yahoo Finance using the following API:

Yahoo Finance Historical Data API: It constructs a URL based on the current time and retrieves the CSV data for the last 10 days.

Example URL: https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=<epoch_ten_days_ago>&period2=<epoch_now>&interval=1d&events=history&includeAdjustedClose=true

Parameters
period1: Start date in Unix epoch time (10 days ago).
period2: End date in Unix epoch time (current date).
interval: Daily interval (1d).
The API returns a CSV file with columns: Date, Open, High, Low, Close, Adj Close, and Volume. The script processes the High and Low prices to calculate the daily average

## Algorithm Explanation
The algorithm used in this script is based on linear regression. Here's a breakdown:

Data Fetching: The script downloads the past 10 days of Bitcoin prices from Yahoo Finance.
Data Preprocessing: It calculates the average price for each day based on the high and low prices.
Linear Regression: The sklearn.linear_model.LinearRegression model is used to predict the price of Bitcoin for the next day. The input (x) is a sequence of numbers representing the days (1-10), and the output (y) is the average price for those days.
Prediction: After training the model, it predicts the price for day 11

## Dependencies
numpy, requests, scikit-learn

