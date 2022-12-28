import numpy as np
import pandas as pd
from numpy.random import seed
np.random.seed = 101

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3,1,2,3]
heir_index = list(zip(outside,inside))
# print(heir_index)
heir_index = pd.MultiIndex.from_tuples(heir_index)
# print(heir_index)

df = pd.DataFrame(np.random.randn(6,2),index=heir_index,columns=['A','B'])
df.index.names = ['Gp','num']
print(df)

# print(df[df.loc['Gp']==1])
# print(df.loc['G1'].loc[1],'\n',df.loc['G2'].loc[1])

# print(df.loc[:,'A'])

print(df.loc['G1']['B'].loc[3])
print(df.loc['G1'].loc[3]['B'])