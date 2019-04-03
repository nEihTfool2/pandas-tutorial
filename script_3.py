# How To Add an Index, Row or Column to a Pandas DataFrame
import pandas as pd 
import numpy as np 

nl = "\n"

arr = np.array([['A', 'B', 'C'],
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

df = pd.DataFrame(data=arr[1:,0:], columns=arr[0])

# Adding an Index to a DataFrame
print(df)
print(nl)

# Set 'C' as the index of the DataFrame
print(df.set_index('C'))
print(nl)

# Adding Rows to a DataFrame
# Differences between loc, iloc and ix
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index=[2, 'A', 4], columns=[48, 49, 50])

# Pass `2` to `loc`
print(df.loc[2])

# Pass `2` to `iloc`
print(df.iloc[2])

# Pass `2` to `ix`
print(df.ix[2])
print(nl)

# Check the differences once more
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index=[2.5, 12.6, 4.8], columns=[48, 49, 50])
print(df)
print(nl)

# There's no index labled `2`, so the index will be changed at position `2`
df.ix[2] = [60, 50, 40]
print(df)
print(nl)

# This will make an index labeled `2` and add the new values
df.loc[2] = [11, 12, 13]
print(df)
print(nl)

# Adding a Column to DataFrame
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

# Use `.index`
df['D'] = df.index
print(df)
print(nl)

# Add a Series to DataFrame with .loc[]
print(df)
print(nl)

# Append column tp `df`
df.loc[:, 4] = pd.Series(['5', '6', '7'], index=df.index)
print(df)
print(nl)

# Resetting the Index of DataFrame
# Messing up index
df = df.set_index('D')
print(df)
print(nl)
# Reset index with `.reset_index()`
df_reset = df.reset_index(level=0, drop=True)
print(df_reset)
print(nl)

print("Replacing `drop` argument by `inplace`")
df.reset_index(level=0, inplace=True)
print(df)
print(nl)