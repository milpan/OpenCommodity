import numpy as np
import pandas as pd

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
    

def efficient_frontier():
    return;
    