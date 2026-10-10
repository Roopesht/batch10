sales_records = [
    {'product': 'Laptop', 'price': 1200, 'quantity': 5},
    {'product': 'Phone', 'price': 800, 'quantity': 10},
    {'product': 'Tablet', 'price': 600, 'quantity': 7}
]

high_value_products = [
    record for record in sales_records 
    if record['price'] > 700
]
print ("High value projects:")
print (high_value_products)

sorted_by_price = sorted(sales_records, key=lambda y: y['quantity'])
print ("Sorted:")
print (sorted_by_price)

