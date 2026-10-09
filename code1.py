import csv

# Reading CSV file
with open('sales_data.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Get headers
    
    for row in reader:
        print(row)

