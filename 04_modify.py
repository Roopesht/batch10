import csv
with open('sales_data.csv', 'r') as file:
    reader = csv.reader(file)
    l1 = []
    for row in reader:
        l1.append(row)

print (l1)
l1[1][1] = '6'
print (l1)
with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(l1)
