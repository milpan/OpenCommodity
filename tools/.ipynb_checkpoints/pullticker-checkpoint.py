import yfinance as yf
import pandas as pd
import datetime
import json
from ast import literal_eval

def pull_symbol(name,period="1y",interval="1d"):
    print("Pulling Information on the Symbol " + name + "/n")
    stock = yf.Ticker(name)
    history = stock.history(period=period, interval=interval)
    return history;

def pull_symbol_name(name):
    stock = yf.Ticker(name)
    stockinfo = stock.info
    #stockparse = literal_eval(stockinfo)
    return stockinfo["shortName"]

def pull_symbol_history():
    return;