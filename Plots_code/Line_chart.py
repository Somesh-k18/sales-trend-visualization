import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Data/sales_trend_data.csv")

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Month'] = df['Date'].dt.month_name() # Month column is created..
print(df.head())

df = sns.lineplot(data=df,x='Month',y='Revenue',hue='Category')

plt.show()



