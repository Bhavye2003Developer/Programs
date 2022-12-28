import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# d = {'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':'abc def ghi xyz'.split()}
# df = pd.DataFrame(d,index=[0,1,2,3])
# print(df)

# print(df['col2'].value_counts(),end = "\n\n")

# # print(df.loc[1:2,'col1':'col3'])

# # print(df['col1'].apply(lambda x: x**2))

# df.sort_values(by='col2',inplace=True)
# print(df)

# np.random.seed = 100
# a = np.random.standard_normal(100)
# b = [i for i in range (100)]

# plt.plot(b,a)
# plt.show()
# print(a)

a = np.arange(0,100)
b = a**2
# plt.subplot(1,2,1) #Multiple plots on same canvas
plt.plot(a,b)
b = a**(1/2)
# plt.subplot(1,2,2)
plt.plot(a,b)
plt.legend(loc=0)
plt.show()