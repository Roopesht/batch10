
def create_bar_chart(data, title="Bar Chart"):
    print(f"\n{title}")
    print("=" * len(title))
    
    max_value = max(data.values())
    max_width = 20  # Maximum bar width
    
    for label, value in data.items():
        bar_length = int((value / max_value) * max_width)
        bar = "█" * bar_length
        #print(f"{label:15} | {bar} {value}")
    print (len(data))

# Example usage
sales_by_product = {
    'Laptop': 6000,
    'Phone': 10400,
    'Tablet': 4200
}

for i in range(10000000):
    sales_by_product["test" + str(i)] = i

print (len(sales_by_product))
create_bar_chart(sales_by_product, "Sales by Product")

