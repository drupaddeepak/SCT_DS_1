import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate Sample Dataset
np.random.seed(42)  # For reproducibility
ages = np.random.randint(0, 100, 1000)  # 1000 random ages between 0 and 100
age_bins = [0, 20, 40, 60, 80, 100]
age_labels = ["0-20", "21-40", "41-60", "61-80", "81-100"]
age_groups = pd.cut(ages, bins=age_bins, labels=age_labels)
population_data = pd.DataFrame({'Age': ages, 'Age Group': age_groups})

# Create Bar Chart for Age Groups
age_group_counts = population_data['Age Group'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
age_group_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Population Distribution by Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Number of People")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Create Histogram for Continuous Age Distribution
plt.figure(figsize=(8, 5))
plt.hist(ages, bins=10, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title("Population Distribution by Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

