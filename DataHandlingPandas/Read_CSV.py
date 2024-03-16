import pandas as pd

#read csv file with comma

# df = pd.read_csv('./Students_exams.csv')

# print(df)
#********************************************************************************************
#read csv file with semicolon

# df = pd.read_csv('./Students.csv' , sep=';') # sep to say panda the separtor as ;

# print(df)
#********************************************************************************************

#read exactly columns & Row 

# df = pd.read_csv('./Students_exams.csv' , usecols=['gender' , 'math score'] , nrows=200)
# print(df)

#********************************************************************************************


#df = pd.read_csv('./Students_exams.csv')


#print(df.head()) ------>>> We can give exactly row like 10
#print(df.tail()) ------>>> We can give exactly row like 10

#********************************************************************************************
# No colums name CSV file -->> use parameter name to set columns name 
# header_name = ['A','B','C','D']
# df = pd.read_csv('./Students_no_cols.csv' , names=header_name)

# print(df)