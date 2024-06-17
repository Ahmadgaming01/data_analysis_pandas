import pandas as pd


df = pd.read_csv("students_exams.csv")

df.rename(
    columns={
        'math score' : 'math_score',
        'reading score' : 'reading_score',
        'writing score':'writing_score'

    },
    inplace= True

)


statics_df = pd.DataFrame(columns=['statics' , 'math' , 'writing' , 'reading' ])

x  = df['math_score'].count()
y  = df['writing_score'].count()
n  = df['reading_score'].count()

row = {
    'statics' : 'count',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

#statics_df = statics_df._append(row, ignore_index=True)

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)

x  = df['math_score'].min()
y  = df['writing_score'].min()
n  = df['reading_score'].min()

row = {
    'statics' : 'min',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)
x  = df['math_score'].max()
y  = df['writing_score'].max()
n  = df['reading_score'].max()

row = {
    'statics' : 'max',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)



x  = df['math_score'].mean()
y  = df['writing_score'].mean()
n  = df['reading_score'].mean()

row = {
    'statics' : 'mean',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)

x  = df['math_score'].mean()
y  = df['writing_score'].mean()
n  = df['reading_score'].mean()

row = {
    'statics' : 'mean',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)

x  = df['math_score'].median()
y  = df['writing_score'].median()
n  = df['reading_score'].median()

row = {
    'statics' : 'median',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)


x  = df['math_score'].mode()[0]
y  = df['writing_score'].mode()[0]
n  = df['reading_score'].mode()[0]

row = {
    'statics' : 'mode',
    'math' : x,
    'writing' : y,
    'reading' : n,

}

statics_df = pd.concat([statics_df , pd.DataFrame.from_records([row])] , ignore_index= True)

print(statics_df)

