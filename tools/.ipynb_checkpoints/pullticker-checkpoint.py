import yfinance as yf
import pandas as pd
import datetime

def pull_symbol(name):
    print("Pulling Information on the Symbol " + name + "/n")
    stock = yf.Ticker(name)
    history = stock.history(period="1y", interval="1h")
    return history;

def pull_symbol_history():
    return;