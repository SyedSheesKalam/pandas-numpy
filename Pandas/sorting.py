import pandas as pd
# Sorting Data
# Sorting Data in 1 column sort_values()
# df.sort_values(by = "Column_Name", for accending order we have to pass True, for decendind = False, inplace = True)
df = pd.read_csv("Shees_Data.csv")
df.sort_values(by="Name", ascending=True, inplace=True)
print(df.to_string(index=False))

# Sorting Data in many columns sort_values()
print(df)


