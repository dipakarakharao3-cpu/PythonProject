# import module
import pandas as pd
from IPython.display import display

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],

                          'Age': [30, 35, 37, 33, 34, 30],

                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],

                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
# display(dataFrame)
# ## Salary greater or equal to 100000 and Age < 40 and their JOB starts with ‘D’ from the dataframe ##
display(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
                    ['Name','JOB']])


## Having Salary lesser or equal to 100000 and Age < 40, and their JOB starts with ‘C’ from the dataframe. ##
display(dataFrame.query('Salary  <= 100000 & Age < 40 & JOB.str.startswith("C").values'))


# ## Salary lesser or equal to 100000 and Age < 40 and their JOB starts with ‘P’ from the dataframe ##
display(dataFrame[(dataFrame['Salary']>=100000) & (dataFrame['Age']<40) & dataFrame['JOB'].str.startswith('P')]
      [['Name','Age','Salary']])


# ## all rows having Salary lesser or equal to 100000 and Age < 40 and their JOB starts with ‘A’ from the dataframe. ##
print(dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")])




## Here will get all rows having Salary greater or equal to 100000 and Age < 40 and their JOB starts with ‘D’
# from the data frame. We need to use NumPy

import pandas as pd
import numpy as np
from IPython.display import display

dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                    '  ROSS    ', 'CHANDLER', ' JOEY    '],

                           'Age': [30, 35, 37, 33, 34, 30],

                           'Salary': [100000, 93000, 88000, 120000, 94000, 95000],

                           'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                   'IT', 'ARTIST']})

 # filter dataframe
filtered_values = np.where(
     (dataFrame['Salary'] >= 100000) & (dataFrame['Age'] < 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
display(dataFrame.loc[filtered_values])



## "query " method all rows having Salary lesser or equal to 100000 and Age < 40, and their
# JOB starts with ‘C’ from the dataframe.

from IPython.display import display 
import pandas as pd
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],

                          'Age': [30, 35, 37, 33, 34, 30],

                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],

                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
display(dataFrame.query('Salary  <= 100000 & Age < 40 & JOB.str.startswith("C").values'))
# print(dataFrame.query('Salary  <= 99000 & Age < 37'))
print(dataFrame.query('Salary >=94000 & Age >=30 & JOB.str.startswith("A").values'))


