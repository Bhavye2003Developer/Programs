import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
print(df.isna().sum())
# df.dropna(inplace=True)
print(df.dropna(thresh=3),end="\n\n")
print(df,end="\n\n")
print(df.fillna(value=97))
print(df.dtypes)