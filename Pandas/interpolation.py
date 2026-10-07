import pandas as pd
data= {
    'Score': [30, 60, None, 120, 150, 180, None, 240, 270, None],
    'Wickets': [1,2,3,None,None,6,7,8,9,10]
}
df = pd.DataFrame(data)
df.to_excel("Numeric_Data.xlsx", index=False)

"""
linear
polynomial
time
at-least you have to know
"""
df = pd.DataFrame(data)
df.interpolate(method='linear', axis=0,inplace=True)
print(df)
"""
1- Timer Series data
2- Numeric data with trends
3- avoid dropping rows
"""
