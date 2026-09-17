import pandas as pd                                              ###indexing dataset ###
data =pd.read_csv("nba.csv",index_col="Name")
# print("Dataset")
# print(data.head(5))

# first = data["Age"]                                              ### Selecting a single column ###
# print("\n single column selected from Dataset")
# print(first.head(5))

# first = data[["Age","College","Salary"]]                      ### selecting Multiple column from Dataset ###
# print("\n Multiple column selected from Dataset")
# print(data.head(7))

# import pandas as pd                                             ### Indexing with loc label based indexing ####
# data = pd.read_csv("nba.csv",index_col="Name")
# row = data.loc["Avery Bradley"]
# print(row)

#                                                                  ### selecting Multiple Rows by label ###
# row = data.loc["Avery Bradley"]
# print(row)

#                                                                   ### Selecting Specific Rows and columns ##
# Selection = data.loc[["Avery Bradley","Amir Johnson"],["Team","Position"]]
# print(Selection)

                                                                  ### Selecting all Rows and Specific Columns ###
# all_rows_Specific_columns = data.loc[:,["Team","Position","Salary"]]
# print(all_rows_Specific_columns)

                                                                ### indexing with iloc[] position based indexing ###
# row = data.iloc[3]
# print(row)

                                                                #### Selecting Multiple Rows by Position ###
# rows = data.iloc[[3,5,7]]
# print(rows)

                                                             ### Selecting Specific Rows ND Columns by position ###
# Selection = data.iloc[[3,4,5,8],[1,2,3,4]]
# print(Selection)

                                                        ### Selecting all Rows and Specific Columns by position ###
# Selection =data.iloc[:,[1,2,3,6]]
# print(Selection)

