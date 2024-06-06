import pandas as pd


df = pd.read_csv('students_exams.csv')


func_1 = df.std(numeric_only=True) # sranderd deviation

print(func_1)

func_2 = df.mode() #most value in the data
print(func_2)