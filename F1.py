import matplotlib as plt
import pandas as pd
str = "----------------------------------------------------------------------\n"


#computing annualized returns
def annualized_returns(returns):
    c = returns/100
    rpm = (c+1).prod()**(1/(c.shape[0]))-1
    anr = (rpm+1)**12 -1
    print(str)
    print("Annualized returns are :\n")
    print(anr)
    return anr


# Computing volatility
def volatility(returns):
    c = returns/100
    vol = c.std()*(12**(.5))
    print(str)
    print("Volatilities are :\n")
    print(vol)
    return vol


#computing drawdowns
def drawdowns(returns):
    st = 1000   # Started with Rs.1000
    c = returns/100
    wi = st*(1+c).cumprod()
    pk = wi.cummax()
    drawdown = (wi-pk)/pk
    print(str)
    print("Drawdowns are")
    print(drawdown.min())
    print("\nDrawdown indexes are")
    print(drawdown.idxmin())
    k = pd.DataFrame([wi,pk,drawdown])
    return k



returns = pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv',parse_dates=True,header = 0,index_col=0, na_values=-99.99)
#changing to date format
returns.index = pd.to_datetime(returns.index,format = "%Y%m")
returns.index = returns.index.to_period('M')

drawdowns(returns)
volatility(returns)
annualized_returns(returns)





