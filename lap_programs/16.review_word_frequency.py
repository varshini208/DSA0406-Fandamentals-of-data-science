from collections import Counter
import re
# Customer reviews
reviews = [
    "This product is good",
    "This product is very good",
    "Good product and good quality"
]
# Combine all reviews
text = " ".join(reviews)

# Convert to lowercase and extract words
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# Calculate word frequency
frequency = Counter(words)

# Display the result
print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)