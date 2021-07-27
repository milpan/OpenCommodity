#This file contains all the functions in order to calculate Relative Strengh Metrics

def relative_strength(historicaldata, emarange):
    #Calculate the difference in the close price
    delta = historicaldata['Close'].diff()
    #Seperate the difference between up and down
    tick_up = delta.clip(lower=0)
    tick_down = delta.clip(upper=0)*-1.
    #Calculate the exponential moving average
    ema_tick_up = tick_up.ewm(com=(emarange-1),adjust=False).mean()
    ema_tick_down = tick_down.ewm(com=(emarange-1), adjust=False).mean()
    #Skip range of EMA since this period is used to collect data on the RS
    return (ema_tick_up/ema_tick_down)[emarange:];

def relative_strength_index(historicaldata, emarange):
    rs = relative_strength(historicaldata, emarange)
    return (100 - (100/(1+rs)));