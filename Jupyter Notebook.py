# Task 1: Data Loading and Exploration
import pandas as pd

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Display first few rows of the dataset
data.head()

# Check for missing values and data types
data.info()

# Summary statistics for numerical columns
data.describe()

# Handle missing values (if any)
# Example: Dropping rows with missing values
data_cleaned = data.dropna()

# Task 2: Basic Data Analysis

# Group by 'job' and calculate the mean duration for each job type
job_grouped = data_cleaned.groupby('job')['duration'].mean()
job_grouped

# Group by 'marital' and calculate the mean of 'duration'
marital_grouped = data_cleaned.groupby('marital')['duration'].mean()
marital_grouped

# Task 3: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line chart (if applicable, e.g., trends in duration over months)
plt.figure(figsize=(10, 6))
sns.lineplot(x='month', y='duration', data=data_cleaned)
plt.title('Duration over Months')
plt.xlabel('Month')
plt.ylabel('Duration')
plt.show()

# 2. Bar chart: Average duration by job type
plt.figure(figsize=(10, 6))
sns.barplot(x=job_grouped.index, y=job_grouped.values)
plt.title('Average Duration by Job Type')
plt.xlabel('Job Type')
plt.ylabel('Average Duration')
plt.xticks(rotation=90)
plt.show()

# 3. Histogram: Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(data_cleaned['age'], kde=True, bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Duration vs Campaign
plt.figure(figsize=(10, 6))
sns.scatterplot(x='duration', y='campaign', data=data_cleaned)
plt.title('Duration vs Campaign')
plt.xlabel('Duration')
plt.ylabel('Campaign')
plt.show()

# Task 4: Findings and Observations
# You can summarize insights from the analysis here. For example:
print("Findings and Observations:")
print("1. The average duration seems to vary significantly across different job types.")
print("2. There seems to be a concentration of younger individuals (aged 25-40) in this dataset.")
print("3. Some job types show a higher number of successful campaigns.")

