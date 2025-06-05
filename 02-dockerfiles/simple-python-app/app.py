import pandas as pd

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
}
df = pd.DataFrame(data)

# Print the DataFrame
print("\nSample DataFrame:\n")
print(df)

# Basic statistics
print("\nSummary Statistics:\n")
print(df.describe(include='all'))
