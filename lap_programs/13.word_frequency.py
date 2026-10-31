from collections import Counter
from pathlib import Path
import re
# Read the text file from the same folder
file_path = Path(__file__).with_name("sample_text.txt")
with open(file_path, "r") as file:
    text = file.read()

# Convert to lowercase and extract words
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# Calculate word frequency
frequency = Counter(words)

# Display the result
print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)