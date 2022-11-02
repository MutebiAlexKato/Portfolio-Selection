# Script that is used to calculate the risk..
# of a portfolio of equities.
from itertools import combinations
import pandas as pd
import statistics as st  



def portfolio_risk(port, data):
	""" this function is used to calculate the risk (standard deviation) of a portfolio
	it takes in 2 arguments;
	port -> the portfolio whose risk is to be calculated
	data -> data frame containing the returns of each individual component in the portfolio """

	portfolio = list(combinations(port,2))

	#Assuming equal weighting
	weight = (1/len(port))

	cross = 0 # Risk due to the correlations between stocks in the portfolio
	individual = 0 #Individual risk of each stock in the portfolio
    
	for x in portfolio:
		#Getting the correlations between the returns of the stocks in the portfolio
		correlations = 2*data[x[0]].corr(data[x[1]])*st.stdev(data[x[0]])*st.stdev(data[x[1]])*(weight**2)
		cross = cross + correlations
        
	for m in port:
 		# Standard deviation of the indivdual stocks in the portfolio
		stds = (st.stdev(data[m]))**2
		individual = individual + (stds*(weight**2))
        
	risk = cross + individual
	return risk





