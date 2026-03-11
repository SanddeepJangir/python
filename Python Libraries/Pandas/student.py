# create a data and export in csv and excel file

student = {
    "student_id" : [1,2,3,4,5,6,7,8,9,10],
    "student_name" : ['ram','shyam','rishi','vikas','abhishek','sandeep','kushagra','mehul','deepak','govind'],
    "course" : ['python developer','java developer', 'mern stack developer', 'data engineer','data analyst','data science',
                'data science','data engineer','mern stack developer','java developer'],
    "course_duration" : ["6 month","10 month","8 month","9 month","7 month", "11 month","11 month","7 month","8 month","10 month"],
    "total_fees" : [40000,60000,50000,55000,45000,65000,65000,45000,50000,60000]
}

df = pd.DataFrame(student)
df

# export the data in csv file
df.to_csv("student.csv")

# export the data in excel file
df.to_excel("student.xlsx")
