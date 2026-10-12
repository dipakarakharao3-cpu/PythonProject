## 1. Joining DataFrames Using .join() ##
import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32]}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])

df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])

print(df, "\n\n", df1)

D = df.join(df1)
print("\n\n", D)


## Now we use how = 'outer' in order to get union ##

import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Key':['K0', 'K1', 'K2', 'K3']}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)

df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])


print(df, "\n\n", df1)
res2 = df.join(df1, on='Key')
print(res2)


## 3. Joining DataFrames with Different Index Levels (Multi-Index) ##
import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22]}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))

index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                   names=['key', 'Y'])

df1 = pd.DataFrame(data2, index= index)


print(df, "\n\n", df1)
result = df.join(df1, how='inner')
print(result)