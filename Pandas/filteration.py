"""
1- Select specific columns .
2- filter rows.
3-combine multiple conditions
"""
# 1- Select specific columns
import pandas as pd
df = pd.read_excel("Shees_Data.xlsx")

# print("Select specific columns:")
# print(df[['Name']])
# print(df[['Name','Age', 'Salary']])

# 2- filter rows.
high_Salary = df[df['Salary'] >=50000]
print(high_Salary)

# Filtering rows salary > 50k & age > 30
filtered = df[(df['Age'] >24) & (df['Salary']>50000)]
print("Employees which age is greater then 24 and their salary above 50k")
print(filtered)

# Using OR condition 
filtered_OR = df[(df['Age'] <26) |(df["Performance Score"]>60)]
print(filtered_OR)