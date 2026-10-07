import pandas as pd
df = pd.read_csv("shees_data.csv")
print("sample data set:")
print(df)


print("Description Statistics:")
print(df.describe())