import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data = {
    "Age": [23, 25, 28, 30, 32, 35, 27, 29, 31,
            33, 26, 24, 36, 38, 40, 22, 34, 28],

    "Fat": [18, 20, 22, 25, 27, 29, 21, 23, 24,
            26, 19, 17, 30, 32, 35, 16, 28, 22]
}
df = pd.DataFrame(data)
# Calculate statistics
print("Mean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStandard Deviation:")
print(df.std())

# Boxplots
df.boxplot()
plt.title("Boxplot of Age and Body Fat")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["Fat"])
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.title("Age vs Body Fat")
plt.show()

# Q-Q plots
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

stats.probplot(df["Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()