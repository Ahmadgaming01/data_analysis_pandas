import pandas as pd

df = pd.read_csv('students_exams.csv')

desc = df.describe()

print(desc)