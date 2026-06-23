import pandas as pd


# Read CPI Data From CSV File

df = pd.read_csv('python-practice/June 2026/analyzing-economic-data/cpi-release.csv')
df.head()


# Filtering Indent Level

df = df[df['Indent-Level'] < 3]

df = df.reset_index(drop=True)   


# Removing Unwanted Columns & Renaming Columns

df = df.drop(columns=['Relative-importance-Apr.2026', 
                      'SU-index-May2025', 
                      'SU%-Apr.2026-May2026', 
                      'SA%-Feb.2026-Mar.2026', 
                      'SA%-Mar.2026-Apr.2026', 
                      'SA%-Apr.2026-May2026', 
                      ]
            )

df = df.rename(columns={'Expenditure-category': 'Category', 
                        'SU-index-Apr.2026': 'April Index (Seasonally Unadjusted)', 
                        'SU-index-May2026': 'May Index (Seasonally Unadjusted)', 
                        'SU%-May2025-May2026': 'May YoY% (Seasonally Adjusted)'
                        }
                )


# Adding Delta & Month-over-Month Change

df['Delta'] = df['May Index (Seasonally Unadjusted)'] - df['April Index (Seasonally Unadjusted)']


# Dropped 'SU%-Apr.2026-May2026' to practice MoM% calculations

df['MoM% Change'] = (
    df['Delta'] /
    df['April Index (Seasonally Unadjusted)']
) * 100


# Rearrange Columns

df = df[['Category', 
         'April Index (Seasonally Unadjusted)', 
         'May Index (Seasonally Unadjusted)', 
         'Delta', 
         'MoM% Change', 
         'May YoY% (Seasonally Adjusted)'
         ]]       


# Print Dataframe

print(df)