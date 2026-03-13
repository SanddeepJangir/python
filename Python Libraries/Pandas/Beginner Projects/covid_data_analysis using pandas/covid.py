import pandas as pd

df = pd.read_csv("/content/covid_toy - covid_toy.csv")
df

# top data fetch, we will use df.head(), by default it returns top 5 rows
df.head()

# top data fetch, we will use df.head(), by default it returns last 5 rows
df.tail()

# if you want random indexed data, then we will use df.sample(), by default it return single rows
df.sample()

# if we want to check data type of each column df.dtypes
df.dtypes

# if you want to check overall information then we will df.info()
df.info()

# if you want yo check statical view of data, then you can use df.describe()
df.describe()

df.head(2)

# if you want to check missing data in df, then you will use df.isnull().sum()
df.isnull().sum()  # here fever has 10 missing values.

df['fever'] = df['fever'].fillna(df['fever'].mean())

# df.isnull().sum()

# if you have categorical data , you want to check total sub-categories then
# we will use df['column_name'].value_counts()

df['gender'].value_counts()

df['gender'] = df['gender'].map({"Female": 1 , "Male" : 0})

df['cough'] = df['cough'].map({"Mild": 1, "Strong" : 0})

df['has_covid'] = df['has_covid'].map({"No": 0 , "Yes" : 1})

df['city'] = df['city'].map({"Kolkata": 1,"Bangalore": 2, "Delhi": 3, "Mumbai" : 4})

df.head()


     age	gender	fever	cough	city	has_covid
0	   60	    0	    103.0	  1	   1	   0
1	   27	    0	    100.0	  1	   3	   1
2	   42	    0	    101.0	  1	   3	   0
3	   31	    1	    98.0	  1	   1	   0
4	   65	    1	    101.0	  1	   4	   0
