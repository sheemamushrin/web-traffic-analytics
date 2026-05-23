import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("traffic_data.csv")

# Display first rows
print(data.head())

# Basic statistics
print("\nSummary Statistics:")
print(data.describe())

# Page views analysis
page_views = data['PageViews'].sum()
print("\nTotal Page Views:", page_views)

# Average session duration
avg_duration = data['SessionDuration'].mean()
print("Average Session Duration:", avg_duration)

# Plot page views
plt.figure(figsize=(8,5))
data['PageViews'].plot(kind='hist')
plt.title("Page Views Distribution")
plt.xlabel("Page Views")
plt.ylabel("Frequency")
plt.show()
