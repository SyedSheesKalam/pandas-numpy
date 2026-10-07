""" how to see rows
head(n) or without n it will show 5 rows of starting from top
tail(n) or without n it will show 5 rows of starting from bottom
"""
import pandas as pd
data = pd.read_json("sample_Data.json", encoding='latin1')
print(data.head(10))
print(data.tail(10))