import numpy as np
import pandas as pd
df =pd.read_csv("sales_data_sample.csv", encoding='latin1' )
print(df.head())

# Checking for null values
print(df.isnull().sum())

df['ORDERNUMBER'] = df['ORDERNUMBER'].interpolate(method='linear')
df['ORDERNUMBER'] = df['ORDERNUMBER'].astype(int)

df['QUANTITYORDERED'] = df['QUANTITYORDERED'].fillna(df['QUANTITYORDERED'].mean())

df['PRICEEACH'] = df['PRICEEACH'].fillna(df['PRICEEACH'].mean())

df['ORDERLINENUMBER'] = df['ORDERLINENUMBER'].fillna(df['ORDERLINENUMBER'].mode()[0])

df['SALES'] = df['SALES'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')
df['SALES'] = df['SALES'].fillna(df['SALES'].mean())

df['ORDERDATE']= pd.to_datetime(df['ORDERDATE'], errors= 'coerce')
df['ORDERDATE'] = df['ORDERDATE'].interpolate(method='linear')

df['STATUS'] = df['STATUS'].fillna(df['STATUS'].mode()[0])

df['QTR_ID'] = df['QTR_ID'].fillna(df['QTR_ID'].mode()[0])

df['MONTH_ID'] = df['MONTH_ID'].fillna(df['MONTH_ID'].mode()[0])

df['YEAR_ID'] = df['YEAR_ID'].fillna(df['YEAR_ID'].mode()[0])

df['PRODUCTLINE'] = df['PRODUCTLINE'].fillna(df['PRODUCTLINE'].mode()[0])

df['MSRP'] = df.groupby('PRODUCTLINE')['MSRP'].transform(lambda x: x.fillna(x.mean()))

df['PRODUCTCODE'] = df['PRODUCTLINE'].map(df.groupby('PRODUCTLINE')['PRODUCTCODE'].agg(lambda x: x.mode()[0]))

df['CUSTOMERNAME'] = df.groupby('PHONE')['CUSTOMERNAME'].transform(lambda x: x.ffill().bfill())
df['CUSTOMERNAME'] = df['CUSTOMERNAME'].fillna('Unknown')

df['PHONE'] = df.groupby('CUSTOMERNAME')['PHONE'].transform(lambda x: x.ffill().bfill())
df['PHONE'] = df['PHONE'].fillna('Unknown')

df['ADDRESSLINE1'] = df.groupby('CUSTOMERNAME')['ADDRESSLINE1'].transform(lambda x: x.ffill().bfill())
df['ADDRESSLINE1'] = df['ADDRESSLINE1'].fillna('Unknown')

df['ADDRESSLINE2'] = df['ADDRESSLINE2'].fillna('')

df['CITY'] = df.groupby('CUSTOMERNAME')['CITY'].transform(lambda x: x.ffill().bfill())
df['CITY'] = df['CITY'].fillna('Unknown')

df['STATE'] = df.groupby(['CITY', 'COUNTRY'])['STATE'].transform(lambda x: x.ffill().bfill())
df['STATE'] = df['STATE'].fillna('N/A')

df['POSTALCODE'] = df.groupby('CITY')['POSTALCODE'].transform(lambda x: x.ffill().bfill())
df['POSTALCODE'] = df['POSTALCODE'].fillna('Unknown')

df['COUNTRY'] = df.groupby('CUSTOMERNAME')['COUNTRY'].transform(lambda x: x.ffill().bfill())
df['COUNTRY'] = df['COUNTRY'].fillna('Unknown')

df['TERRITORY'] = df.groupby('CUSTOMERNAME')['TERRITORY'].transform(lambda x: x.ffill().bfill())
df['TERRITORY'] = df['TERRITORY'].fillna('Unknown')

df['CONTACTLASTNAME'] = df.groupby('CUSTOMERNAME')['CONTACTLASTNAME'].transform(lambda x: x.ffill().bfill())
df['CONTACTLASTNAME'] = df['CONTACTLASTNAME'].fillna('Unknown')

df['CONTACTFIRSTNAME'] = df.groupby('CUSTOMERNAME')['CONTACTFIRSTNAME'].transform(lambda x: x.ffill().bfill())
df['CONTACTFIRSTNAME'] = df['CONTACTFIRSTNAME'].fillna('Unknown')

df['DEALSIZE'] = df['DEALSIZE'].fillna( pd.qcut(df['SALES'], q=3 , labels=['Small', 'Medium', 'Large']))

print(df[df.duplicated(keep=False)].head())
df = df.drop_duplicates()
print("Duplicates: ", df.duplicated().sum())

print("Infinity values: ", np.isinf(df.select_dtypes(include=[np.number])).sum().sum())

print("Shape of the DataFrame: ", df.shape)

print(df.isnull().sum())

df.to_csv("cleaned_sales_data.csv", index=False)


