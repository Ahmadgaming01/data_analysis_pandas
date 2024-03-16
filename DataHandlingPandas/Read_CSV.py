import pandas as pd

#read csv file 
# df = pd.read_csv('./Students_exams.csv')

# print(df)

# df = pd.read_csv('./Students.csv' , sep=';') # sep to say panda the separtor as ;

# print(df)

df = pd.read_csv('./Students_exams.csv' , usecols=['gender' , 'math score'] , nrows=200)
print(df)