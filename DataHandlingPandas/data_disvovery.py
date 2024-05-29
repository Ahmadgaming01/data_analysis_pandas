import pandas as pd


df = pd.read_csv('students_exams.csv')
print(df.info())
print(df.isnull())
print(df.isnull().sum())
