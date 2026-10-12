## Sorting single column by Age Default in Ascending order ##

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 40],'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Age')
print("Sorting in Ascending order:""\n",sorted_df)

# Sorting in Descending order ##
sorted_df = df.sort_values(by='Age',ascending=False)
print("\n\n",sorted_df)


## Sorting a DataFrame by Multiple Columns: ##
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by=['Age', 'Score'])
print("\n\n",sorted_df)



## Sorting DataFrame with Missing Values: ##
import pandas as pd
data_with_nan = {"Name": ["Alice", "Bob", "Charlie", "David"],"Age": [28, 22, None, 22]}
df_nan = pd.DataFrame(data_with_nan)

sorted_df = df_nan.sort_values(by="Age", na_position="first")
print(sorted_df)



## Sorting by Index ##
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)
df_sorted_by_index = df.sort_index()
print(df_sorted_by_index)


## sort by index in descending order by passing the ascending=False argument. ##

df_sorted_by_index_desc = df.sort_index(ascending=False)
print(df_sorted_by_index_desc)



## Choosing a Sorting Algorithm ##
# 1) QuickSort (kind='quicksort'): It is a highly efficient, divide-and-conquer sorting algorithm ##
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [28, 22, 25, 22, 28],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Age', kind='quicksort')
print(sorted_df)



## 2) MergeSort (kind='mergesort'):  ##

sorted_df = df.sort_values(by='Age', kind='mergesort')
print(sorted_df)

## 3) HeapSort (kind= 'heapsort'): ##

sorted_df = df.sort_values(by='Age', kind='heapsort')
print(sorted_df)




## Applying Custom Sorting Logic:##

import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [28, 22, 25, 22, 28],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Name', key=lambda col: col.str.lower())
print(sorted_df)

import pandas as pd
D1 = {"Name": ["Alice","Bob","Charlie","Davide","Eve"],
      "Age": [28,21,25,22,38],
      "Score" : [85,100,45,78,90]}
df = pd.DataFrame(D1)
sorted_df = df.sort_values(by='Age',kind='mergesort')
print(sorted_df)