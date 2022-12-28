import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
y = pd.Series([np.random.randint(1,10) for i in range(30)])
x = pd.Series([i for i in range(-len(y),len(y)+1)]) 

# sns.pairplot(y,x)
# sns.countplot(x=x,y=y)
# plt.plot(x,y)
# y.sort()
# y.sort_values()
print(list(y))
print(y.value_counts())
print(y.nunique())
print(f"Mean : {np.mean(y)}")
print(f"Median : {np.median(y)}")
print(y.value_counts().head(1))

# plt.hist(y)
# sns.barplot(y)
# plt.subplot(1,2,1)
sns.histplot(y,legend=True,binrange=(1,9))
# plt.subplot(1,2,2)
# plt.plot(x,(x**(1/2)))
# sns.countplot(data=y)
# plt.hist2d(x,y)
plt.grid()
plt.show()