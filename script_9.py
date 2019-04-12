# When, Why And How to Reshape Pandas DataFrame
import numpy as np 
import pandas as pd 

# Pivotting DataFrame
products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                        'store': ['Walmart', 'Dia', ' Walmart', 'Fnac', 'Dia', 'Walmart'],
                        'price': [11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                        'testscore': [4, 3, 5, 7, 5, 8]})
# Use 'pivot()' to pivot the DataFrame
pivot_products = products.pivot(index='category', columns='store', values='price')

# Check out the result
print(pivot_products)
print('\n')

# Pivot DataFrame without values specifically filled in
pivot_products = products.pivot(index='category', columns='store')
print(pivot_products)
print('\n')

# Pivot 'products' DataFrame with 'pivot_table()'
pivot_products = products.pivot_table(index='category', columns='store', values='price', aggfunc='mean')
print(pivot_products)
print('\n')

# Using stack() and unstack() to Reshaped Pandas DataFrame
# Row Multi-Index
row_idx_arr = list(zip(['r0', 'r0'], ['r-00', 'r-01']))
row_idx = pd.MultiIndex.from_tuples(row_idx_arr)

# Column Multi-Index
col_idx_arr = list(zip(['c0', 'c0', 'c1'], ['c-00', 'c-01', 'c-10']))
col_idx = pd.MultiIndex.from_tuples(col_idx_arr)

# Create the DataFrame
d = pd.DataFrame(np.arange(6).reshape(2,3), index=row_idx, columns=col_idx)
d = d.applymap(lambda x: (x // 3, x % 3))
print(d)
print('\n')
# Stack/Unstack
s = d.stack()
u = d.unstack()
print(s)
print('\n')
print(d)
print('\n')

# Reshape DataFrame with melt()
# 'people' DataFrame
people = pd.DataFrame({'FirstName' : ['John', 'Jane'],
                        'LastName' : ['Doe', 'Austen'],
                        'BloodType' : ['A-', 'B+'],
                        'Weight' : [90, 64]})

# Use 'melt()' on the 'people' DataFrame
print(pd.melt(people, id_vars=['FirstName', 'LastName'], var_name='measurements'))