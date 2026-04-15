import pandas as pd
import numpy as np

# encoding ---> get_dummies --->
#  use for small data set and increase data due to heavy machine learning model

# column ----> has_covid['Yes','No']  ---> When we apply get_dummies --->
# 2 columns create --> has_covid_yes, has_covid_no

df = pd.read_csv('/content/insurance - insurance.csv')

df.head(3)

a = pd.get_dummies(df,columns=['sex','smoker','region'])

a = a.astype(int)
# a

# if I have multiple sub-categories --- 1 column drop --- data multiconielity
# issue resolve
# model --> overfitting -->
# 1 student ----> 2 days exam ---> exam paper --> exam clear
# but 3 days ---> question answer --> xxx

b = pd.get_dummies(df,columns=['sex','smoker','region'],drop_first=True)
b = a.astype(int)

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop='first',sparse_output=False,dtype=np.int32)

ohe.fit_transform(df[['sex','smoker','region']])


# b
