import csv
# Using DictReader for better structure
with open('sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['product'], row['sales'])
