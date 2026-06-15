import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Data/sales_trend_data.csv")

# Convert Date Column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print("=" * 50)
print("SALES TREND VISUALIZATION REPORT")
print("=" * 50)

# --------------------------------------------------
# 1. Total Revenue
# --------------------------------------------------
total_revenue = df['Revenue'].sum()
print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

# --------------------------------------------------
# 2. Total Quantity Sold
# --------------------------------------------------
total_quantity = df['Quantity'].sum()
print(f"Total Quantity Sold: {total_quantity}")

# --------------------------------------------------
# 3. Revenue by Category
# --------------------------------------------------
print("\nRevenue by Category:")
category_revenue = (
    df.groupby('Category')['Revenue']
      .sum()
      .sort_values(ascending=False)
)

print(category_revenue)

# --------------------------------------------------
# 4. Revenue by City
# --------------------------------------------------
print("\nRevenue by City:")
city_revenue = (
    df.groupby('City')['Revenue']
      .sum()
      .sort_values(ascending=False)
)

print(city_revenue)

# --------------------------------------------------
# 5. Top 10 Products by Revenue
# --------------------------------------------------
print("\nTop 10 Products by Revenue:")

top_products = (
    df.groupby('Product')['Revenue']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)

# --------------------------------------------------
# 6. Best Selling Product
# --------------------------------------------------
print("\nBest Selling Product:")

best_selling = (
    df.groupby('Product')['Quantity']
      .sum()
      .sort_values(ascending=False)
      .head(1)
)

print(best_selling)

# --------------------------------------------------
# 7. Highest Revenue Order
# --------------------------------------------------
print("\nHighest Revenue Order:")

highest_order = df.loc[df['Revenue'].idxmax()]
print(highest_order)

# --------------------------------------------------
# 8. Monthly Revenue Trend
# --------------------------------------------------
monthly_sales = (
    df.groupby(df['Date'].dt.month)['Revenue']
      .sum()
)

# --------------------------------------------------
# Visualization 1
# Monthly Revenue Trend
# --------------------------------------------------
plt.figure(figsize=(10, 5))

monthly_sales.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

plt.savefig("monthly_revenue_trend.png")
plt.show()

# --------------------------------------------------
# Visualization 2
# Revenue by Category
# --------------------------------------------------
plt.figure(figsize=(8, 5))

category_revenue.plot(
    kind='bar'
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()

# --------------------------------------------------
# Visualization 3
# Revenue Distribution by Category
# --------------------------------------------------
plt.figure(figsize=(8, 8))

category_revenue.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Revenue Distribution by Category")
plt.ylabel("")

plt.savefig("category_pie_chart.png")
plt.show()

# --------------------------------------------------
# Visualization 4
# Top Products
# --------------------------------------------------
plt.figure(figsize=(12, 6))

top_products.plot(
    kind='bar'
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

print("\nAnalysis Completed Successfully!")