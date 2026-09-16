import pandas as pd
data =pd.read_csv("/content/nba.csv",index_col="Name")
print("Dataset")
print(data.head(5))