import pandas as pd
df1 = pd.DataFrame({
    "employee_id": [1, 2, 3, 4, 5]
})
df2 = pd.DataFrame({
    "name": ["Addi", "Bob", "Charlie", "Farhana", "Eve"],
    "age": [30, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000]
})

# new_table = pd.merge(df1, df2, on="employee_id", how="inner")
# print(new_table)

# contentation of two dataframes
new_Table_2= pd.concat([df1, df2], axis=1, ignore_index=True)
print(new_Table_2)