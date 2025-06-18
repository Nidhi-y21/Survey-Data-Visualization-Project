import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Survey schema: Age group, Gender, Satisfaction (1-5), Platform used, Frequency, Recommend (Yes/No)
n = 500  # number of responses
age_groups = ['Under 18', '18-25', '26-35', '36-50', '50+']
genders = ['Male', 'Female', 'Other']
platforms = ['Mobile App', 'Website', 'Email']
frequencies = ['Daily', 'Weekly', 'Monthly', 'Rarely']
recommend = ['Yes', 'No']

data = {
    'Age Group': np.random.choice(age_groups, n),
    'Gender': np.random.choice(genders, n),
    'Satisfaction': np.random.randint(1, 6, n),  # Ratings 1 to 5
    'Platform Used': np.random.choice(platforms, n),
    'Usage Frequency': np.random.choice(frequencies, n),
    'Would Recommend': np.random.choice(recommend, n)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("survey_data.csv", index=False)

# Set visual style
sns.set(style="whitegrid")

# Bar chart: Count by Age Group
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Age Group', palette='muted', order=df['Age Group'].value_counts().index)
plt.title('Survey Responses by Age Group')
plt.ylabel('Count')
plt.xlabel('Age Group')
plt.tight_layout()
plt.savefig("age_group_bar.png")
plt.show()

# Pie chart: Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Gender Distribution')
plt.tight_layout()
plt.savefig("gender_pie.png")
plt.show()

# Bar chart: Average Satisfaction by Platform
platform_satisfaction = df.groupby('Platform Used')['Satisfaction'].mean().sort_values()
plt.figure(figsize=(8, 5))
sns.barplot(x=platform_satisfaction.values, y=platform_satisfaction.index, palette='coolwarm')
plt.title('Average Satisfaction by Platform')
plt.xlabel('Average Satisfaction')
plt.ylabel('Platform Used')
plt.tight_layout()
plt.savefig("satisfaction_by_platform.png")
plt.show()

# Heatmap: Cross-tab between Age Group and Recommend
cross_tab = pd.crosstab(df['Age Group'], df['Would Recommend'], normalize='index')
plt.figure(figsize=(8, 5))
sns.heatmap(cross_tab, annot=True, cmap='YlGnBu', fmt='.1%')
plt.title('Recommendation Rate by Age Group')
plt.ylabel('Age Group')
plt.xlabel('Would Recommend')
plt.tight_layout()
plt.savefig("recommendation_heatmap.png")
plt.show()
