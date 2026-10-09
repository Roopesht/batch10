import csv
data = [ ['cpu',5,20000,100000] ]
with open('sales_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


