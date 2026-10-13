import pandas as pd
n = int(input("Enter number of sales records: "))
products = []
quantities = []

for i in range(n):
    print("\nRecord", i + 1)
    products.append(input("Enter product name: "))
    quantities.append(int(input("Enter quantity sold: ")))

df = pd.DataFrame({
    "Product": products,
    "Quantity": quantities
})
total_sales = df.groupby("Product")["Quantity"].sum()
top5 = total_sales.sort_values(ascending=False).head(5)
print("\nTop 5 Best-Selling Products:")
print(top5)