import pandas as pd
n = int(input("Enter number of orders: "))
customer = []
date = []
product = []
quantity = []
for i in range(n):
    print("\nEnter details for order", i + 1)
    customer.append(int(input("Customer ID: ")))
    date.append(input("Order Date (YYYY-MM-DD): "))
    product.append(input("Product Name: "))
    quantity.append(int(input("Order Quantity: ")))
order_data = pd.DataFrame({
    "Customer_ID": customer,
    "Order_Date": pd.to_datetime(date),
    "Product_Name": product,
    "Order_Quantity": quantity
})
print("\nTotal orders by each customer:")
print(order_data.groupby("Customer_ID").size())
print("\nAverage quantity for each product:")
print(order_data.groupby("Product_Name")["Order_Quantity"].mean())
print("\nEarliest order date:", order_data["Order_Date"].min())
print("Latest order date:", order_data["Order_Date"].max())