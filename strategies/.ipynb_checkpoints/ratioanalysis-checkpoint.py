#This strategy uses a reference commodity and measures another commodities ratio compared to its average to decipher wether it is undervalued or overvalued
import numpy as np

def start_ratio(referencehistory, targethistory):
    averageratio = find_average_historical_ratio(referencehistory,targethistory)
    newratio = find_current_ratio(referencehistory,targethistory)
    score = ratio_strategy_score(averageratio,newratio)
    return score;

def find_average_historical_ratio(referencehistory, targethistory):
    '''
    referencehistory --> Pandas Dataframe consisting of the Historical Price Data of the Reference
    targethistory --> Pandas Dataframe consisting of the Target Price Data of the Reference
    '''
    referenceprice = referencehistory['Close'].to_list()
    targetprice = targethistory['Close'].to_list()
    averagereference = np.mean(referenceprice)
    averagetarget = np.mean(targetprice)
    return averagetarget/averagereference;

#Finds the average current ratio from the head of the historical data
def find_current_ratio(referencehistory,targethistory):
    '''
    referencehistory --> Pandas Dataframe consisting of the Historical Price Data of the Reference
    targethistory --> Pandas Dataframe consisting of the Target Price Data of the Reference
    '''
    referenceprice = referencehistory['Close'].to_list()
    targetprice = targethistory['Close'].to_list()
    averagereference = referenceprice[-1]
    averagetarget = targetprice[-1]
    return averagetarget/averagereference;

def ratio_strategy_score(historicalratio, currentratio):
    '''
    Returns a score of the current ratio to the historical ratio, where a negative number yields that the current commodity is overvalued compared to historical ratio
    '''
    return (currentratio-historicalratio)*100;