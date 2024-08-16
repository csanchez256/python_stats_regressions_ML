
import pandas as pd

df = pd.read_csv('C:\\Users\\css7c\\OneDrive\\Desktop\\NM Paper Datasests 7.14.24\\SUMMARY_STATISTICS\\Data From Gabriel M 8.14.24\\data\\nm_medicaid_weighted_08_14_2024.csv')

alter_statements = []

for column in df.columns:
    max_length = df[column].astype(str).str.len().max()
    alter_statements.append(f"ALTER TABLE YourTableName ALTER COLUMN {column} VARCHAR({max_length + 10});") # Add some buffer

# Output the statements
with open('alter_statements.sql', 'w') as f:
    f.write('\n'.join(alter_statements))

