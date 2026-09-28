## The merge() function provides flexibility for different types of joins.
#There are four basic ways to handle the join
#(inner, left, right and outer) depending on which rows must retain their data.
# Merging using one key and multiple Keys

import pandas as pd

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)
# print(df, "\n\n", df1)

# Merging common column by using (on) Argument this allows to combine Dataframe where the value in a specific column match.
res = pd.merge(df, df1, on='key')
print("\n\n",res)

# We can also merge DataFrames based on more than one column by passing a list of column names to the on argument.
res1 = pd.merge(df, df1, on=['key', 'key1'])
print("\n\n",res1)


##  Merging DataFrames Using the (how) Argument:
# how = 'left' in order to use keys from left frame only:

res = pd.merge(df, df1, how='left', on=['key', 'key1'])
print("\n\n",res)

# how = 'right' in order to use keys from right frame only:
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])
print("\n\n",res1)

# how = 'outer' in order to get union of keys from dataframes:
res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])
print("\n\n",res2)

# how = 'inner' in order to get intersection of keys from dataframes:
res3 = pd.merge(df, df1, how='inner', on=['key', 'key1'])
print("\n\n",res3)
