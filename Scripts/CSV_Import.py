#=======================================================
# Python script to adjust the column widths in db table
# to fix truncation error in .CSV flat file import
#=======================================================


import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\css7c\\OneDrive\\Desktop\\NM Paper Datasests 7.14.24\\SUMMARY_STATISTICS\\Data From Gabriel M 8.14.24\\data\\nm_medicaid_weighted_08_14_2024.csv')

column_names = []


# for column in df.columns:
#     max_length = df[column].astype(str).str.len().max()
#     alter_statements.append(f"ALTER TABLE NM_Medicaid ALTER COLUMN {column} VARCHAR({max_length + 256});") # Add some buffer



for column in df.columns:
    max_length = df[column].astype(str).str.len().max()
    column_names.append(f"{column} nvarchar({max_length + 10}) NOT NULL,") # Add some buffer

# Try this: https://stackoverflow.com/questions/35003138/python-pandas-inferring-column-datatypes


'''
for name, dtype in df.dtypes.iteritems():
    print(name, dtype)  
'''


# Output the statements
with open('alter_statements.sql', 'w') as f:
    f.write('\n'.join(column_names))

    

# Next: need a way to read in each column name and parse out the data type

# Get a list of columns
#columns = df.columns.tolist()

# Get data types of each column
#data_types = df.dtypes

# Print the columns and their data types
'''
print("Columns:", columns)
print("Data Types:\n", data_types)
'''

'''
for n in columns:
    print('col {},  "data type: {}' .format(columns,data_types))
'''

# Step #1 build a dictionary of colums and data types
# Step #2 run alter table script, to build a SQL query that will preprocess .csv file

