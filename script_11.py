# How To Write a Pandas DataFrame to a File
import pandas as pd 
import numpy as np
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

# Write DataFrame to CSV
df.to_csv('myDataFrame.csv', sep='\t', encoding='utf-8')

# Write DataFrame to Excel
writer = pd.ExcelWriter('myDataFrame.xlsx')
df.to_excel(writer, 'DataFrame')
writer.save()