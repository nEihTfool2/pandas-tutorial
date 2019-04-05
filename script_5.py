# How to Rename the Index or Columns
import numpy as np 
import pandas as pd 

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7,8,9]]), columns=['A', 'B', 'C'])

# Define the new names of columns
newcols = {
    'A': 'new_column_1',
    'B': 'new_column_2',
    'C': 'new_column_3'
}

# Using `rename()` to columns
df.rename(columns=newcols, inplace=True)
print(df)

# Using `rename()` to index
df.rename(index={1: 'a'}, inplace=True)
print(df)