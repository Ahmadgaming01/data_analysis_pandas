import pandas as pd 

df = pd.read_csv('actor_info.csv')

get_country = df.groupby('contry')

#print(get_country.groups)# country & id

#print(get_country.get_group('Germany'))

grby = df.groupby(['contry' , 'amount'])


for group , contry in grby:
    print(group)
    print(contry)


# country number

counts = df.groupby('contry')['id'].count()
#print(counts)


counts_1 = df.groupby(['contry']).agg(mean_amount = ('amount' , 'mean') , sum_amount = ('amount' , 'sum') ,max_amount = ('amount' , 'max') , numbers = ('id' , 'count'))

sort_counts_1 = counts_1.sort_values(by=['sum_amount'] , ascending= False)


print(sort_counts_1)