import pandas as pd

df = pd.read_csv('students_exams.csv')

x= df.std(numeric_only= True)


y = df.mode()

print(y)