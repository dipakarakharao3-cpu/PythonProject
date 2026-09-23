## When we're working with multiple datasets we need to combine them in different ways.
# Pandas provides three simple methods like merging, joining and concatenating

## 1. Concatenating DataFrame using .concat() ##
import pandas as pd
data1 = {'Name':['jai','Princi','Gaurav','Anju'],
         'Age' :[27,24,22,32],
         'Address' :['Nagpur','Kanpur','Allahabad','Kannuaj'],
         'Qualification' :['Msc','MA','MCA','Phd']}

data2 = {'Name':['Abhi','Ayushi','Dhiraj','Hitesh'],
         'Age':[17,14,12,52],
         'Qualification':['Btech','B.A','Bcom','B.hons']}

df = pd.DataFrame(data1, index = [0,1,2,3])
df1 = pd.DataFrame(data2, index = [4,5,6,7])
# print(df,"\n\n",df1)

frames = [df, df1]
res1 = pd.concat(frames)
print(res1)

## 2. Concatenating DataFrames by Setting Logic on Axes ##
# We can modify the concatenation by setting logic on the axes.
# Specifically we can choose whether to take the Union (join='outer') or Intersection (join='inner') of columns.

res2 = pd.concat([df, df1], axis=1, join='inner')
print(res2)

## 3. Concatenating DataFrames by Ignoring Indexes ##
# ignore_index argument. This is useful when we don't want to carry over any index information.

import pandas as pd
data3 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

data4 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

df = pd.DataFrame(data3, index=[0, 1, 2, 3])
df1 = pd.DataFrame(data4, index=[2, 3, 6, 7])

print(df, "\n\n", df1)
res = pd.concat([df, df1], ignore_index=True)
print(res)

# 4. Concatenating DataFrame with group keys : keys argument
frames = [df, df1 ]
res = pd.concat(frames, keys=['x', 'y'])
print(res)


# 5. Concatenating Mixed DataFrames and Series : ere we are going to mix Series and dataframe together.
import pandas as pd
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data1,index=[0, 1, 2, 3])

s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')

print(df, "\n\n", s1)
res = pd.concat([df, s1], axis=1)
print(res)



