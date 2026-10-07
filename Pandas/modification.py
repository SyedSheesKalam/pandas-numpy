# adding columns
import pandas as pd
df = pd.read_excel("Shees_Data.xlsx")
df['Bonus']=df['Salary']*0.1

print(df) 

# using insert
df.insert(0,"Employee_ID",[6122,6123,6125,6126,6127,6121,6040,6049])
print(df)

# Updaying values

df.loc[0,'Salary']= 34000
print(df)

# Increasing Salary by 5%
df['Salary']= df['Salary'] * 1.05
print(df)

# removing column 
df.drop(columns=['Performance Score', 'Bonus'], inplace = True)
# IF write inplace= False it will give us new dataFrame 
# if inplace = True it modify the current dataFrame
print(df)