import pandas as pd

df = pd.read_csv ('students_exams.csv') #select one col from the csv file 


student = df[['gender' , 'math score']]#select more col from the csv file 

rows = df[2:7] # select rows



# loc function 
result = df.loc[0] # to return exactly row
result_b = df.loc[[1, 4 , 888]] # to return more than value


rows_a_col = df.loc[[1,2,5] , ['gender']] #return value to exactly col

rows_b_col = df.loc[:: ,['gender']]
rows_b_col = df.loc[15:30 ,['gender' , 'math score']]


# iloc function

result_c = df.iloc[0] # to return exactly row
result_a = df.iloc[[1,99] , [0,3]]


# in the iloc function we can just use the index of column 
# in the loc function we can use the name of column






