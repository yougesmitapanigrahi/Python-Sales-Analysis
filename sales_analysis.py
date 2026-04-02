import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df['Total'] = df['Quantity'] * df['Price']

print("Total Revenue:", df['Total'].sum())

category_sales = df.groupby('Category')['Total'].sum()
print(category_sales)

category_sales.plot(kind='bar')
plt.show()