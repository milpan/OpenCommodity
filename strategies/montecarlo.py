import numpy as np
import pandas as pd
from functools import reduce

def generate_random_weights(Weights):
    n_weights = len(Weights)
    return np.random.dirichlet(np.ones(n_weights),size=1)

def format_history(list_history, parseby_arg, symbol_name):
    '''
    Formats a list of dictionaries into a single dictionary for suitable format
    list_history = List of History Dictionaries
    parseby_arg = String for which columns to concanate
    symbol_name = List of Symbol names for column headers of dataframe to be made
    '''
    target_frame = pd.DataFrame()
    for history, symbol in zip(list_history, symbol_name):
        history = history[parseby_arg]
        target_frame[symbol] = history
    return target_frame

def portfolio_value(list_history, list_weights, symbol_name):
    TotalValue = []
    for i in range(len(list_history)):
        close_price = list_history[i]['Close']
        weight = list_weights[i]
        TotalValue.append(close_price*weight)
    d = reduce(lambda x, y: x.add(y, fill_value=0), TotalValue)
    return d;

def efficient_frontier(list_history, list_weights, symbol_name, n_iterations):
    portfolioValue = []
    #Generate Random Normal Weights
    for i in range(n_iterations):
        newWeights = generate_random_weights(list_weights)
        #Calculate the portfolio history
        totalHistory = portfolio_value(list_history, newWeights, symbol_name)
        portfolioValue.append(totalHistory)
    return portfolioValue;
    