sales_data = [
    {'product': 'Laptop', 'price': 1200, 'quantity': 5},
    {'product': 'Phone', 'price': 800, 'quantity': 10},
    {'product': 'Tablet', 'price': 600, 'quantity': 7},
    {'product': 'Phone', 'price': 800, 'quantity': 3}
]

# Basic statistics
def calculate_stats(data, field):
    values = [item[field] for item in data]
    return {
        'total': sum(values),
        'average': sum(values) / len(values),
        'maximum': max(values),
        'minimum': min(values),
        'count': len(values)
    }

price_stats = calculate_stats(sales_data, 'quantity')
print(price_stats)