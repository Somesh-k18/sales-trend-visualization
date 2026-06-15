import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/sales_trend_data.csv")

city_sales = df.groupby('City')['Revenue'].sum()

plt.figure(figsize=(8, 8))

plt.pie(
    city_sales,
    labels=city_sales.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Revenue Distribution by City')
plt.show()