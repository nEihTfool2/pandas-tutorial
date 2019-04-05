# How To Format The Data in Pandas DataFrame
import numpy as np 
import pandas as pd 

def print_w_nl(df):
    print(df)
    print('\n')

np_array = np.array([
    ["OK", "Perfect", "Acceptable"],
    ["Awful", "Awful", "Perfect"],
    ["Acceptable", "OK", "Poor"]
])

df = pd.DataFrame(data=np_array, columns=["Student1", "Student2", "Student3"])
print_w_nl(df)

# Replace the Strings by numerical values (0-4)
df.replace(['Awful', 'Poor', 'OK', 'Acceptable', 'Perfect'], [0, 1, 2, 3, 4], inplace=True)
print_w_nl(df)

# Replace strings by others with `regex`
regex_test = pd.DataFrame(data=[['1\n', 2, '3\n'], [4, 5, '6\n'], [7, '8\n', 9]])
print_w_nl(regex_test)
regex_test.replace({'\n': '<br>'}, regex=True, inplace=True)
print_w_nl(regex_test)

# Removing Parts From Strins in the Cells of DataFrame
df = pd.DataFrame(data=np.array([[1, 2, "+3b"], [4, 5, '-6B'], [7, 8, '+9A']]), columns=["class", "test", "result"])
print_w_nl(df)

# Delete unwanted parts from the strings in the `result`column
df['result'] = df['result'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
print_w_nl(df)


# Splitting Text in a Column into Multiple Rows in a DataFrame
df = pd.DataFrame(data=np.array([
    [34, 0, '23:44:55'],
    [22, 0, "66:77:88"],
    [19, 1, "43:68:05 56:34:12"]
]), columns=['Age', 'PlusOne', 'Ticket'])
print_w_nl(df)

# Split out the two values in the third row
# Make it a Series
# Stack the values
ticket_series = df['Ticket'].str.split(' ').apply(pd.Series, 1).stack()
print_w_nl(ticket_series)
# Get rid of the stack:
# Drop te level to line up with the DataFrame
ticket_series.index = ticket_series.index.droplevel(-1)
print_w_nl(ticket_series)

# Make your `ticket_series` a dataframe
ticketdf = pd.DataFrame(ticket_series)
print_w_nl(ticket_series)

# Delete `Ticket`column from DataFrame
del df['Ticket']

# Join the `ticketdf` DataFrame to `df`
df = df.join(ticketdf)
print_w_nl(df)

