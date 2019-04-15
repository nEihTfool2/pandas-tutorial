# How To Iterate Over a Pandas DataFrame
import pandas as pd 
import numpy as np 

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

for index, row in df.iterrows():
    print(row['A'], row['B'])