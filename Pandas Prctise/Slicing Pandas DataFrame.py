import pandas as pd

player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)
                                                         #### Slicing Rows in dataframe ###
df1 = df.iloc[0:4]
print(df1)
                                                        #### Slicing Columns in dataframe ###
df1 = df.iloc[:, 0:2]
print(df1)
                                                        ### Selecting a Specific Cell in a Pandas DataFrame ###
value = df.iloc[2, 3]
print("Specific Cell Value:", value)

                                                       #### Using Boolean Conditions in a Pandas DataFrame ###
data = df[df['Age'] > 35]
print("\nFiltered Data based on Age > 35:\n", data)

df.set_index('Name', inplace=True)


                                                           #### Slicing Rows in Dataframe ###
custom = df.loc['A.B.D Villers':'S.Smith']
print(custom)

                                                          ### Selecting Specified cell in Dataframe ###

value = df.loc['V.Kohli', 'Salary']
print("\nValue of the Specific Cell (V.Kohli, Salary):", value)