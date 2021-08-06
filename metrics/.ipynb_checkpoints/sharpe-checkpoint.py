import pandas as pd

def calculate_sharpe(PortfolioHistory, ListofSymbol):
    iterator = 0;
    #Lets first reorganise our List of Portfolio Data
    for history in PortfolioHistory:
        history['Symbol'] = pd.Series(ListofSymbol[iterator], index=history.index);
        iterator=iterator+1;
    #Concatanate the Result and Pull out the Close and Symbol Info
    result = pd.concat(PortfolioHistory, axis=0)
    result = result[['Close', 'Symbol']]
    return result
            