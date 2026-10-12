import pandas as pd
data = {'Name':['Arika', 'Bob', 'Jai','Arya'],
        'Age':[27, 28, 29, 30],
        'Score':[95,80,85,90]}
df=pd.DataFrame(data)
sorted_df=df.sort_values(by=['Age','Score'])

print(sorted_df)