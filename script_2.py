# How To Select an Index or Column From a Pandas DataFrame
import numpy as np 
import pandas as pd 

arr = np.array([['A', 'B', 'C'],
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

df = pd.DataFrame(data=arr[1:,0:], columns=arr[0])

print('Get value 1')
print("Using 'iloc[]'") #IMPORTANT
print(df.iloc[0][0])
print('\n')

print("Using 'loc[]'") #IMPORTANT
print(df.loc[0]['A'])
print('\n')

print("Using 'at[]'")
print(df.at[0, 'A'])
print('\n')

print("Using 'iat[]'")
print(df.iat[0,0])
print('\n')


print("Selecting rows and columns")
print("Use 'iloc[]' to select row '0'")
print(df.iloc[0])
print('\n')

print("Use 'loc[]' to select column`'A'`")
print(df.loc[:, 'A'])