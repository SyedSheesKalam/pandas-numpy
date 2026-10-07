import pandas as pd
data = {
    "Name": ['Shees',  'Bilal', 'Talha', 'Faiza','Asma','Sareena','Samad','Rumaisa'],
    "Age": [20, 21, 22, 23, 24, 25, 26, 27],
    "Married": [False, True, True, True, True, True, True, True],
    "Salary": [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
    "Performance Score": [90,80, 70, 60, 50, 40, 30, 20]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("Shees_Data.", index=False)

