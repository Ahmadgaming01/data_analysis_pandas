import pandas as pd


df = pd.read_csv('Students_exams.csv')


for index , row in df.iterrows():
    #print(index , row) return index and row from csv
    #print(index , row["gender"]) return index and exactly coloumn
    print()


# itertuple() return all row & every row in tuple that is speed than iterrows()
for row in df.itertuples() :
    print()


#iteration of coloumn



for col in df.columns:
    #print(df[col][2])
    print()

for label , col in df.items(): #old version was iteritems()
    #print(label , col.values)
    print()

for label , col in df[['gender' , 'math score']].items():
    #print(label , col.values)
    print()


result = df.loc[2:5 , ['gender' , 'math score']]
print(result)

for index , row in result.iterrows():
    #print(index , row['gender'] , row['math score'])
    print(index , row.values)
    