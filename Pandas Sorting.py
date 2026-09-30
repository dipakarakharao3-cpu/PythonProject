# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 40],'Score': [85, 90, 95, 80]}
# df = pd.DataFrame(data)
#
# sorted_df = df.sort_values(by='Score', inplace=True)
# print(sorted_df)
#
# #
# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 40],
#         'Score': [85, 90, 95, 80]}
# df = pd.DataFrame(data)
#
# sorted_df = df.sort_values(inplace=['Age', 'Score'])
# print(sorted_df)

import pandas as pd
data = {
    "Name": ["Bob", "Dog", "Charlie", "David", "Apple"],
    "Age": [28, 22, 25, 22, 28],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Name', key=lambda col: col.str.lower())
print(sorted_df)
