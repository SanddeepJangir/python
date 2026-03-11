 # Pandas --> pandas is an open source library which is used for handle data manipulation
import pandas as pd

# data structure of pandas ::::
# (1). series ---> it stores only values not column name and it is one-dimensional
# (2). dataframe ---> it store values with column name. and it is multi-dimensional

a=pd.Series([1,45,78,90])
a

type(a)

# dataframe

a = {
    "EMP_ID" : [1,2,3,4,5],
    "Name" : ['sam','mohit','raj','rahul','aniket'],
    "Department" :['IT','SALES','IT','IT','SALES'],
    "Salary" : [10000,20000,30000,50000,40000]
}

df = pd.DataFrame(a)
df

# export this data into csv

df.to_csv("Emp_data.csv")

# export this data into excel

df.to_excel("New_emp_data.xlsx")

# import the data
a = pd.read_csv("/content/Emp_data.csv")
a
