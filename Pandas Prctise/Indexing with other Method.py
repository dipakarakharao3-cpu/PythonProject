### Useful indexing method in DataFream ####

import pandas as pd
data = pd.read_csv("nba.csv",index_col="Name")
# print("Dataset")
# print(data.head(5))                              ### first n number ###
# print(data.tail(5))                              ### last n number ###
# print(data.describe()

result = data.query(" Age > 30 " and "Weight > 180")      #### Boolean expression ###
print(result)

