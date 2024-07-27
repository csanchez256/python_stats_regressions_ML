# Here's a python script that imports .csv files, and sets the nvarchar limit to the max
# if more than 50 characters exists
# 7/27/24

import csv
with open('C:\\Users\\css7c\\OneDrive\\Desktop\\Python_Programs\\nm_clean.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)