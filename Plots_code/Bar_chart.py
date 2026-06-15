import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Data/sales_trend_data.csv")

category_sales = df.groupby('Category', as_index=False)['Revenue'].sum()

plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_sales,
    x='Category',
    y='Revenue',
    hue='Category',
    legend=False
)

plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue')

plt.tight_layout()
plt.show()