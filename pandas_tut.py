import pandas as pd
import numpy as np

#Series
# l = [1,2,3,4,5]
# l_series = pd.Series(l,index=[i*i for i in range(5)],dtype=float)
# print(l_series)

# d = {'a':[i for i in range(5)],'b':[i**2 for i in range(5)],'c':[i**3 for i in range(5)]}
# d_series = pd.Series(data=d.values(),index=d.keys())
# print(d_series)

# print(d_series)


# a = [10,20,30,40,50]
# b = list(map(chr,filter(lambda x: x<60,a)))
# print(b)


#DataFrames
from numpy.random import randn
np.random.seed(101) #for same values every time

df = pd.DataFrame(data=[[10,20,30],[40,50,60]],columns=['a','b','c'],index=[i*10 for i in range(1,3)],dtype=float)
# print(df)


df = pd.DataFrame(data=randn(5,4),columns=['W','X','Y','Z'],index=['A','B','C','D','E'])
# print(df,end = "\n\n")

# print(df.loc['A'],end = "\n\n")
# print(df.iloc[0],end = "\n\n")

# print(df[['W','Z']])

df['V'] = randn(5,)
# print(df)

df.drop('W',axis=1,inplace=True)
# print(df)

df.drop('E',inplace=True)
# print(df)

#ROWS
# print(df.loc['A':'C'])
# print(df.loc[['A','B']])

# print(df.iloc[:2])

# print(df.loc['A':'C','X':'Z'])
# print(df.iloc[:3,:3])

# print(df.iloc[[0,1,2],:])
print("\n\n",df.loc[['A','B','D'],'X':'Y'],end = "\n\n")
# print(df[df['X']>-0.6])
# print(df[df['X']>-0.6].loc[:,'Y':'V'])


#Multiple conditions
# print(df[(df['X']>0) & (df['Y']>0.5)])

# df.index = range(0,df.shape[0])
df.reset_index(inplace=True) #To reset the index to original 0-n-1 range
df.drop('index',axis=1,inplace=True)
# print(df)

states = 'CA NY WY OR'.split()
df['States'] = states
# df.index = states
# or
df.set_index('States',inplace=True)
print(df)