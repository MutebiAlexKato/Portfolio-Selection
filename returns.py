#Script used to calculate the returns of a given...
#... portfolio of equities.

from itertools import combinations
import pandas as pd 
import statistics as st 


def portfolio_returns(port, data):
	""" This function is used to calculate the returns of a given portfolio.
	It takes in two arguments;
	port -> portfolio whose returns are to be calculated 
	data -> data frame containing returns for each individual stock. """

	# Assuming equal weighting in every portfolio,
	weight = (1/len(port))
	Sum = 0
	for i in port:
		Sum = Sum + st.mean(data[i])
		returns = Sum*weight

	return returns




