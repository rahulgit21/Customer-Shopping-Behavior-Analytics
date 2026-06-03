import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\CUSTOMER SHOPPING PROJECT\DATASET\customer_shopping_behavior.csv")

print(df.head())
df.info()
df.isnull().sum()
df.dropna(inplace=True)

#####Sales by Category

category_sales = df.groupby("Category")["Purchase Amount (USD)"].sum()

category_sales.plot(kind='bar')

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.show()

#####Gender Spending Distribution

gender_sales = df.groupby("Gender")["Purchase Amount (USD)"].sum()

gender_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Gender Spending Distribution")
plt.ylabel("")

plt.show()

##Seasonal Sales Trend



season_sales = df.groupby("Season")["Purchase Amount (USD)"].sum()

season_sales.plot(kind='line', marker='o')

plt.title("Seasonal Sales Trend")
plt.xlabel("Season")
plt.ylabel("Total Sales")

plt.show()

##### Age Distribution of Customers

df["Age"].plot(kind='hist', bins=10)

plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.show()

##### Payment Method Usage

payment_method = df["Payment Method"].value_counts()

payment_method.plot(kind='bar')

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.show()

##### Top Purchased Items

top_items = df["Item Purchased"].value_counts().head(10)

top_items.plot(kind='bar')

plt.title("Top 10 Purchased Items")
plt.xlabel("Items")
plt.ylabel("Number of Orders")

plt.show()