import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = 'netflix_titles.csv'
data = pd.read_csv(file_path)

# Display basic info
print(data.head())
print(data.info())

# Clean and convert the `date_added` column
# Strip extra spaces and handle errors gracefully
data['date_added'] = data['date_added'].str.strip()  # Remove leading/trailing spaces
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')  # Coerce invalid dates to NaT

# Verify conversion
print(data['date_added'].head())

# Example Visualization: Number of Movies and TV Shows by Year
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='type', order=data['type'].value_counts().index, palette="viridis")
plt.title('Count of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Example Visualization: Distribution of Release Years
plt.figure(figsize=(12, 8))
sns.histplot(data=data, x='release_year', bins=30, kde=True, color='blue', alpha=0.7)
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.show()
