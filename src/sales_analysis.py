import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/sales_data.csv')

# Show first rows
print("First 5 Rows:")
print(df.head())

# Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Product-wise sales
product_sales = df.groupby('Product')['Sales'].sum()
print("\nSales by Product:")
print(product_sales)

# Region-wise sales
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(region_sales)

# Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

# Monthly Sales Graph
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('images/monthly_sales.png')
plt.show()

# Product Sales Graph
plt.figure(figsize=(8,5))
product_sales.plot(kind='bar')
plt.title('Product-wise Sales')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.savefig('images/product_sales.png')
plt.show()

# Region Sales Graph
plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title('Region-wise Sales')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.savefig('images/region_sales.png')
plt.show()

print("\nProject Completed Successfully")
