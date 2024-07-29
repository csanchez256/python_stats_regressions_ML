# Here's a python script that imports .csv files, and sets the nvarchar limit to the max
# if more than 50 characters exists
# 7/27/24

import csv
with open('C:\\Users\\css7c\\OneDrive\\Desktop\\Python_Programs\\nm_clean.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# https://realpython.com/python-csv/

with open('C:\\Users\\css7c\\OneDrive\\Desktop\\Python_Programs\\nm_clean.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        
        line_count += 1
    print(f'Processed {line_count} lines.')        