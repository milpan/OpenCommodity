import pandas as pd
from strategies import *
import matplotlib.pyplot as plt

def calculate_sharpe(PortfolioHistory, ListofSymbol):
    '''
    Calculate the Sharpe Ratio of a List of Portfolio History
    '''
    PctChange = []
    meanPctChange = []
    stdPctChange = []
    outputSharpe = pd.DataFrame()
    newHistory = format_history(PortfolioHistory, "Close", ListofSymbol)
    #calculate the change in each symbol
    for symbolName in ListofSymbol:
        outputSharpe[f'Pct Change {symbolName}'] = newHistory[symbolName].pct_change() * 100
        outputSharpe[f'Mean {symbolName}'] = outputSharpe[f'Pct Change {symbolName}'].rolling(365, min_periods=2).mean()
        outputSharpe[f'Std {symbolName}'] = outputSharpe[f'Pct Change {symbolName}'].rolling(365, min_periods=2).std()
        outputSharpe[f'Sharpe {symbolName}'] = (outputSharpe[f'Mean {symbolName}']/outputSharpe[f'Std {symbolName}']) * np.sqrt(365)
        #calculate the mean of this percentage change
        plt.plot(outputSharpe.index[100:],outputSharpe[f'Sharpe {symbolName}'][100:], label=symbolName)
    plt.legend()
    plt.show()
    return outputSharpe;
            