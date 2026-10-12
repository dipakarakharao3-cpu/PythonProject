
## 2. Joining DataFrames Using the "on" Argument ##

import pandas as pd
data1={'Name':['Jai', 'Prachi','Gaurav', 'Anju'],
      'Age' :[27,24,22,32],
      'key' :['k0','k1','k2','k3']}

data2={'Address':['Akola','Mumbai','Nagpur','Delhi'],
       'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2,index=['K0', 'K2', 'K3','k4'])

print(df,"\n\n",df1)
res2 = df.join(df1,on='key')
print("\n\n", res2)