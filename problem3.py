import pandas as pd


df = pd.read_csv('original_data.csv')  
print(df.columns[1:])

req_df = df.melt(id_vars=['Year'], var_name='Month', value_name='Value')
original_months_order = list(df.columns[1:])  
# print(original_months_order)
req_df['Month'] = pd.Categorical(req_df['Month'],categories=original_months_order, ordered=True)
req_df = req_df.sort_values(['Year','Month'])

req_df.to_csv('transposed_datan.csv',index=False)

