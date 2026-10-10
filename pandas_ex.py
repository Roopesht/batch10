import pandas as pd

# Create DataFrame from CSV
df = pd.read_csv('sales_data.csv')

# Basic operations
print(df.head())  # First 5 rows
print(df.describe())  # Statistical summary
print(df.groupby('product').sum())  # Group by product

# Advanced analysis
df['total_revenue'] = df['price'] * df['qty']
monthly_sales = df.groupby('product')['total_revenue'].sum()

# Export results
df.to_csv('processed_sales.csv', index=False)