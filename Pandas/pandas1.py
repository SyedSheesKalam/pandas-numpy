import pandas as pd
#read json file into a DataFrame
df = pd.read_json("sample_Data.json", encoding='latin1')
# print(df.head())
# print(df.shape)
print(df)