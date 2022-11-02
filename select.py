# This script is used to construct different portfolions...
# providing the returns and standard deviation of each portfolio

from itertools import combinations
import pandas as pd
import statistics as st  
import risk as rk
import returns as rt


# Dummy data for testing
Stocks = ['A','B','C','D'] # Individual stocks that can be put in a portfolio.

x = [1,0,3,4]
y = [2,3,-4,5]
z = [3,-9,5,6]
w = [4,20,6,7]
dt = {'A':x,'B':y,'C':z,'D':w}
data  = pd.DataFrame(dt) #Dummy data for testing

def portfolio_selection(stocks, number):
	# Function to buld different portfolios
	# Takes in two agruments
	# stocks -> individual stocks that can be put in a portfolio
	# number -> number of stocks in a portfolio

	returns = {}
	risk = {}

	portfolio = list(combinations(stocks,number))

	for i in portfolio:
		returns[i] = rt.portfolio_returns(i,data)
		risk[i] = rk.portfolio_risk(i,data)

	data_frame = {'Portfolio':list(risk.keys()), 'Returns': list(returns.values()), 'Risk': list(risk.values())}

	return pd.DataFrame(data_frame)

result = portfolio_selection(Stocks, 2)

print(result)	



