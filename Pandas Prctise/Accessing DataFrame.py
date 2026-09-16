                                                     ### How to access csv file in system  ###
# import pandas as pd
# df = pd.read_csv("data.csv")
# print(df.head())
#
#                                                    ### Display the entire DataFrame print(df) ###
import pandas as pd
data = {'Name': ['Rahul','Amit','Sagar','Riya'],
        'Age' : [25,30,35,31],
        'Gender':['Male','Male','Male','Female'],
        'Salary':[50000,75000,35000,60000]}
df = pd.DataFrame(data)
# print(df)
                                                        ### Access the age column ###
# age_column = df['Age']
# print(age_column)
#
                                                        ### Accessing Rows by Index "1" ###
Second_row = df.loc[1]
print(Second_row)

#                                                          ### Accessing Multiple Rows or column ###
# Subset = df.loc[0:2,['Name','Age']]
# print(Subset)

#                                                          ### Accessing Rows Based on Conditions ###
# filter_data = df[df['Age']>=30]
# print(filter_data)

                                                        ### Accessing Specific Cells with at[] ###
# Salary_at_index_2 = df.at[2,'Salary']
# print("Salary is : ",Salary_at_index_2)
