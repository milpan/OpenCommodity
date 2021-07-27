#This strategy uses a reference commodity and measures another commodities ratio compared to its average to decipher wether it is undervalued or overvalued

def start_ratio(referencesymbol,):
    return;

def find_average_historical_ratio(referencehistory, targethistory):
    '''
    referencehistory --> Pandas Dataframe consisting of the Historical Price Data of the Reference
    targethistory --> Pandas Dataframe consisting of the Target Price Data of the Reference
    '''
    referenceprice = referencehistory['Close']
    targetprice = targethistory['Close']
    
    averagereference = referenceprice.mean()
    averagetarget = targetprice.mean()
    return averagetarget/averagereference;

#Finds the average current ratio from the head of the historical data
def find_average_current_ratio(referencehistory,targethistory):
    return;

def ratio_strategy_score(historicalratio, currentratio):
    return;