import pandas as pd
#  Aggregation in Pandas
# summary statistics of data using aggregation functions like sum(), mean(), max(), min(), count() etc.
df = pd.read_csv("Shees_Data.csv")
# df_agg = df[['Name', 'Age', 'Salary']].max()
# df_agg = df[['Name', 'Age', 'Salary']].count()
df_agg = df[['Name', 'Age', 'Salary']].sum()
print(df_agg)
