import pandas as pd

df1 = pd.DataFrame({
    'column_a':[1,2,3,4],
    'column_b':['a','b','g','w'],
    'column_c':[True , False , True , False]
    
})


df2 = pd.DataFrame({
    'column_a':[3,7,9,3],
    'column_b':['y','c','k','q'],
    'column_c':[False , True , False , True]
    
})

df = pd.concat([df1 , df2] ,keys=['df1' , 'df2'] ,axis= 1 )

df_merge = pd.merge(df1 , df2 , on='column_a') #merge the column with same name 

df2.rename(columns={'column_a':'new_column_a'} , inplace= True)

df_merge2 = pd.merge(df1 , df2 , left_on='column_a' , right_on='new_column_a') #merge the column with diff. name 


