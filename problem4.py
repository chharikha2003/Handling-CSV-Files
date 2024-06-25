import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('TicketData.csv')
df['Category'] = df['Category'].str.strip().str.lower()
cate_grp=df.groupby('Category').size().reset_index(name='count')
print(cate_grp)

cate_grp =cate_grp.sort_values(by='count', ascending=False)
cate_grp['Cumulative Percentage'] = (cate_grp['count'].cumsum()/ cate_grp['count'].sum()) * 100

plt.figure(figsize=(6,4))
plt.bar(cate_grp['Category'],cate_grp['count'])
plt.plot(cate_grp['Category'],cate_grp['Cumulative Percentage'])
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Count of Tickets by Category')
plt.xticks(rotation=90) 
plt.show()