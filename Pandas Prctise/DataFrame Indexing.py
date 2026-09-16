                                                         ## Dataframe from list:
#
# import pandas as pd
# lst= ['apple','ball','cat','dog','fish']
# df= pd.DataFrame(lst)
# print(df)
#
                                                          # # ## DataFrame from dict of Numpy Array:
#
# import pandas as pd
# import numpy as np
# data = {'A': np.array([1,4,7]),
#         'B': np.array([2,5,8]),
#         'C': np.array([3,6,9])}
# df = pd.DataFrame(data)
# print(df)
#
                                                             # ##Dataframe from List of dictionaries:
# import pandas as pd
# data = [{'Name' : 'Mike','Degree':'Mca','Score': 90},
#         {'Name' : 'Dani','Degree':'BA','Score': 80},
#         {'Name' : 'sumit','Degree':'BE','Score': 70}]
# df = pd.DataFrame(data)
# print(df)
# print(df.index)

#                                                             ### Pandas DataFrame index ###
# import pandas as pd
# data = {'Name': ['Jake', 'Eve', 'Charlie'],
#         'Age': [ 22, 35, 28],
#         'Gender': [ 'Male', 'Female', 'Male'],
#         'Salary': [40000, 70000, 48000]}
# df = pd.DataFrame(data)
# # print(df.index)
# # print(df)
#
#
# res = df.set_index('Age')                                   ### setting custom index ###
# # res = df.reset_index(drop=True)                          ### Resetting the index ###
# print(res)
#
# #
# import pandas as pd
# data = {'age': [25, 30], 'city': ['NY', 'LA']}                  # #indexing with loc ##
# df = pd.DataFrame(data, index=['Alice', 'Bob'])
# row = df.loc['Alice']
# print(row)
#
# import pandas as pd                                               ## loc label based indexing ##
# data ={'Name': ['Arika','Amit','Aarti'],
#         'Age' : [1,34,28],
#         'Gender': ['Female','Male','Female']}
# df = pd.DataFrame(data)
# res = df.set_index('Name')
# # row =df.loc['Arika']
# print(res)

