# import numpy as np
# import pandas as pd

# d = {'A':[1,1,2,2,3,3],'B':['ab','ab','ab','cd','cd','cd']}
# df = pd.DataFrame(d)
# print(df)
# a = df.groupby(by=['B','A'])
# print(a.head())

import os
# print(os.getcwd())
# a = os.path.join(os.getcwd(),"__pycache__")
# os.chdir(a)
# print(os.listdir())

a = []
b = []
c = []
os.chdir("/bin")
for i,j,k in os.walk(os.getcwd()):
    a.append(i)
    b.append(j)
    c.append(k)


print(a)
print(b)
# print(c[0])