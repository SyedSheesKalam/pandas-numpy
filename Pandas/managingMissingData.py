import pandas as pd
"""
NaN (Not a Number)
None (for object data type)

isnull()
True - NaN is missing
False - Value is present
"""
df = pd.read_excel('Shees_Data.xlsx')
# print(df)

# print(df.isnull().sum())

# # drop any missing value of column or row
# df.dropna(axis = 0, inplace=True)
# print(df)

# Fill default value
# df = df.astype(object)
# df.fillna(0, inplace=True)
# print(df)

# Filling Conditional values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
print(df)



