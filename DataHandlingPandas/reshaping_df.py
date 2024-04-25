import pandas as pd

df1 = pd.DataFrame({
'City':['Frankfurt','Berlin','Hamburg',],
'First_day' :[22 , 22,28], 
'second_day':[15 ,17,24], 
'third_day' :[18 , 24,22], 
'fourth_day':[24 ,14,26], 
'fifth_day' :[21 , 12,15], 

})

city = df1.melt(id_vars=['City'] , var_name='day' , value_name='temprature').sort_values(by='City')
print(city)