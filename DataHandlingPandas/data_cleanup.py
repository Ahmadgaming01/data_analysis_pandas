import pandas as pd

df = pd.read_csv('students_exams.csv')

print(df.columns)

df.columns = [col.lower() for col in df]
print(df.columns)

df.rename(
    columns = {
        'math score':'math_score',
        'reading score':'reading_score',
        'writing score' : 'writing_score',

    },inplace=True
)
print(df)