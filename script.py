import numpy as np

# A structured array
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
# Print the sctructured array
print(my_array['foo'])

# A record array
my_array2 = my_array.view(np.recarray)
# Print the record array
print(my_array2.foo)