import pandas as pd

# Read CPI Data From CSV File

df = pd.read_csv('cpi-release.csv')
df.head()

# Filter Out Data
df[df['Indent-Level'] < 3]

df2 = df.filter(items=['Indent-Level', 
                       'Expenditure-category', 
                       'SU-index-Apr.2026', 
                       'SU-index-May2026', 
                       'SU%-Apr.2026-May2026']
                )

df = df2[df2['Indent-Level'] < 3]

print(df)