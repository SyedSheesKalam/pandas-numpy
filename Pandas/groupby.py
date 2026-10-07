import pandas as pd 

data ={
    "name": ["Addi", "Bob", "Charlie", "Farhana", "Eve"],
    "age": [30, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
grouped = df.groupby("age")["salary"].sum()
print(grouped)

# MULTIPLE COLUMNS GROUPED
grouped_multiple = df.groupby(["name", "age"])["salary"].sum()
print(grouped_multiple)