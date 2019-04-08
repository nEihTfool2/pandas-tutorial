# How To Create an Empty DataFrame
import pandas as pd 
import numpy as np 

# creating empty DataFrame with numpy.nan (has dtype float)
df = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
print(df)

# creating empty DataFrame with forced dtype
df = pd.DataFrame(index=range(0,4), columns=['A'], dtype='float')
print(df)

df2 = pd.DataFrame(index=range(0,4), columns=['A'], dtype='str')
print(df2)

df3 = pd.DataFrame(index=range(0,9), columns=['B'], dtype='datetime64')
print(df3)