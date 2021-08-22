import pandas as pd

def calculate_sharpe(PortfolioHistory, ListofSymbol):
    #method is clunky, will refine this soon...
    iterator = 0;
    newHistory = []
    PctChange = []
    meanPctChange = []
    stdPctChange = []
    for history in PortfolioHistory:
        temphistory = pd.DataFrame(data=history['Close'])
        iterator=iterator+1;
        newHistory.append(temphistory)
    #concatanate the result into one large dataframe
    result = pd.concat(newHistory, axis=1)
    iterator = 1;
    #set the appropriate labels
    result.columns = ListofSymbol
    #calculate the change in each symbol
    for history in newHistory:
        history['PctChange'] = history['Close'].pct_change() * 100
        #calculate the mean of this percentage change
        history['Mean'] = history['PctChange'].rolling(365, min_periods=2).mean()
        history['Std'] = history['PctChange'].rolling(365, min_periods=2).std()
        history['Sharpe'] = history['PctChange']/history['Std']

    return newHistory;
            