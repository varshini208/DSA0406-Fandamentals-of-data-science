# %%
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

# Read CSV file
from pathlib import Path

file_path = Path(__file__).with_name("data.csv")
df = pd.read_csv(file_path)

# Stop words
stop_words = ["the", "and", "is", "a", "to", "of", "in", "this"]

# Preprocess feedback
words = []

for feedback in df["feedback"]:
    text = str(feedback).lower()
    text = re.sub(r'[^a-z\s]', '', text)

    for word in text.split():
        if word not in stop_words:
            words.append(word)

# Calculate frequency
frequency = Counter(words)

# Get top N words
n = int(input("Enter top N words: "))
top_words = frequency.most_common(n)

print("Top Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Plot bar graph
word_names = [item[0] for item in top_words]
word_counts = [item[1] for item in top_words]

plt.bar(word_names, word_counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top N Frequent Words")
plt.show()