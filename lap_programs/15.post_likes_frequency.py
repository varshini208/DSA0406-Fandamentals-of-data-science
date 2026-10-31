import pandas as pd
# Create a DataFrame
data = {
    "Post_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Likes": [50, 100, 50, 200, 100, 50, 150, 200]
}
df = pd.DataFrame(data)
# Calculate frequency distribution of likes
frequency = df["Likes"].value_counts().sort_index()

# Display the result
print("Frequency Distribution of Post Likes:")
print(frequency)