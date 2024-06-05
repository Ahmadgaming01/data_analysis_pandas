import pandas as pd


df = pd.read_csv('students_exams.csv')
# print(df.info())
# print(df.isnull())
# print(df.isnull().sum())


for col in df[['math score' , 'reading score' , 'writing score']]: # convert the value to numeric , if impossable return nan
    df[col] = pd.to_numeric(df[col] , errors = 'coerce')


df = df.dropna(subset=['reading score'])
# print(df.isnull().sum())


df['gender'].fillna(value='Unkown' , inplace=True) # applay the fillna on exactly column 
#print(df.head(5))

for col in df[['math score' , 'reading score' , 'writing score']]:
    df[col].fillna(value=df[col].mean() , inplace= True) # applay mean value of column where value nan
    print(df)


df['writing score'] = df['writing score'].where(df['writing score']<100 , 75)
print(df)
