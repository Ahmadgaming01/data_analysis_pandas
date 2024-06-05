import pandas as pd


df = pd.read_csv('students_exams.csv')

count_value = df['math score'].count() 

print(count_value)

min_value = df['math score'].min()
print(min_value)

max_value = df['math score'].max()

print(max_value)

mean_value = df['math score'].mean() #return avrage of the values

print(mean_value)

median_value = df['math score'].median()#return avrage of the values 
print(median_value)

quantile_25 = df['math score'].quantile(0.25)
print(quantile_25)


quantile_50 = df['math score'].quantile(0.5)
print(quantile_50)


quantile_75 = df['math score'].quantile(0.75)
print(quantile_75)