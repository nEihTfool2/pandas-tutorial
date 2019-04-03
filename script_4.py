# How to Delete Indices, Rows or Columns From a Pandas Data Frame
import pandas as pd 
import numpy as np 

def nl():
    print('\n')

# Deleting Index from Dataframe

# remove duplicate index values by resetting index, dropping duplicates and resintating duplicateless column as index
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), index=[2.5, 12.6, 4.8, 4.8, 2.5], columns=[48, 49, 50])
df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')

# Deleting Column from DataFrame
print(df)
nl()

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]]), columns=['A', 'B', 'C'])
# Drop the column with label 'A'
df.drop('A', axis=1, inplace=True)
print(df)
nl()

# Drop column at position 1
print(df.drop(df.columns[1], axis=1))
nl()

# Removing a Row from DataFrame
df = pd.DataFrame(data=np.array([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 6], [23, 50, 60, 7], [23, 35, 37, 23]]), index=[2.5, 12.6, 4.8, 4.8, 2.5], columns=[48, 49, 50, 50])
df.drop_duplicates([48], keep='last', inplace=True)
print(df)
nl()

# Using drop if there is no uniqueness criterion o the deletion
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]]), columns=['A', 'B', 'C'])
print(df.drop(df.index[1]))


# Always consider resetting the index
df.reset_index(inplace=True)