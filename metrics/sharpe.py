import pandas as pd
from strategies import *
import matplotlib.pyplot as plt

def calculate_sharpe(PortfolioHistory, ListofSymbol):
    '''
    Calculate the Sharpe Ratio of a List of Portfolio History
    PortfolioHistory = List of Historical Price Data in Dataframe Format
    ListofSymbol = List of symbol names for the Plotting
    '''
    PctChange = []
    meanPctChange = []
    stdPctChange = []
    outputSharpe = pd.DataFrame()
    arraySharpe = []
    newHistory = format_history(PortfolioHistory, "Close", ListofSymbol)
    #calculate the change in each symbol
    fig, ax = plt.subplots(figsize=(12,8))
    for symbolName in ListofSymbol:
        outputSharpe[f'Pct Change {symbolName}'] = newHistory[symbolName].pct_change() * 100
        outputSharpe[f'Mean {symbolName}'] = outputSharpe[f'Pct Change {symbolName}'].rolling(365, min_periods=2).mean()
        outputSharpe[f'Std {symbolName}'] = outputSharpe[f'Pct Change {symbolName}'].rolling(365, min_periods=2).std()
        outputSharpe[f'Sharpe {symbolName}'] = (outputSharpe[f'Mean {symbolName}']/outputSharpe[f'Std {symbolName}']) * np.sqrt(365)
        #Remove outliers from the data
        outputSharpe = outputSharpe[outputSharpe[f'Sharpe {symbolName}'] < 4]
        outputSharpe = outputSharpe[outputSharpe[f'Sharpe {symbolName}'] > -4]
        arraySharpe.append(outputSharpe[f'Sharpe {symbolName}'])
        ax.plot(outputSharpe.index[20:],outputSharpe[f'Sharpe {symbolName}'][20:], label=symbolName)
    ax.set_xlabel("Date")
    ax.set_ylabel("Sharpe Ratio")
    plt.legend()
    plt.show()
    return outputSharpe;
            