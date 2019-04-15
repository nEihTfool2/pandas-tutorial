# Does Pandas Recognize Dates When Importing Data?
import pandas as pd 
import numpy as np 

# TODO: Make actually use of following code on a self created examples CSV with dates

# read csv and set parse_dates to True to recognize dates
pd.read_csv('file', parse_dates=True)

# alternative option:
pd.read_csv('file', parse_dates=['colName'])

# construct own parser if there are uncommon date-time formats
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

# include
pd.read_csv(infile, parse_dates=['colName'], dateparser=dateparse)

# Or combine two columns into a single DateTime column
pd.read_csv(infile, parse_dates={'datetime': ['date', 'time']}, date_parser=dateparse)