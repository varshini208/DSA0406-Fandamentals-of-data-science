import pandas as pd
n = int(input("Enter number of properties: "))
property_id = []
location = []
bedrooms = []
area = []
price = []

for i in range(n):
    print("\nEnter property", i + 1, "details:")
    property_id.append(int(input("Property ID: ")))
    location.append(input("Location: "))
    bedrooms.append(int(input("Number of bedrooms: ")))
    area.append(float(input("Area in square feet: ")))
    price.append(float(input("Listing price: ")))

property_data = pd.DataFrame({
    "Property_ID": property_id,
    "Location": location,
    "Bedrooms": bedrooms,
    "Area": area,
    "Price": price
})
print("\nAverage listing price by location:")      # 1. Average listing price in each location
print(property_data.groupby("Location")["Price"].mean())

print("\nProperties with more than 4 bedrooms:")   # 2. Properties with more than four bedrooms
print(len(property_data[property_data["Bedrooms"] > 4]))

print("\nProperty with the largest area:")         # 3. Property with the largest area
print(property_data.loc[property_data["Area"].idxmax()])