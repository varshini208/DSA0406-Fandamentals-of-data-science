import pandas as pd
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [20, 25, 20, 30, 25, 20, 35, 30]
}
df = pd.DataFrame(data)

# Find frequency distribution of customer ages
frequency = df["Age"].value_counts().sort_index()

# Display the result
print("Frequency Distribution of Customer Ages:")
print(frequency)