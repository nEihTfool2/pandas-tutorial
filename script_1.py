# 1. How To Create a Pandas DataFrame
import numpy as np 
import pandas as pd 

# Make data frame from a NumPay array
data = np.array([['', 'Col1', 'Col2'],
                ['Row1', 1, 2],
                ['Row2', 3, 4]])

print(pd.DataFrame(data=data[1:, 1:],
                    index=data[1:, 0],
                    columns=data[0, 1:]))
print("\n")

print("Take a 2D array as input to DataFrame")
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))
print("\n")

print("Take a dictionary as input to DataFrame")
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict))
print("\n")

print("Take a Dataframe as input to DataFrame")
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(my_df)
print("\n")

print("Take a Series as input to DataFrame")
my_series = pd.Series({"Belgium": "Brussels", "India": "New Delhi", "United Kingdom": "London", "United States": "Washington"})
print(pd.DataFrame(my_series))
print("\n")

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the 'shape' property
print(df.shape)

# Or use tje 'len()' function with the 'index' property
print(len(df.index))

print(list(df.columns.values))