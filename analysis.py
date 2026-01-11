import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv('vegetarian_foods.csv')


# Display top 5 rows
print(df.head())


# Top 5 high-protein foods
print(df.sort_values('Protein (g)', ascending=False).head())


# Top 5 low-calorie foods
print(df.sort_values('Calories').head())


# Average nutrients
print(df.mean())


# Bar chart: Top 5 high-protein foods
top_protein = df.sort_values('Protein (g)', ascending=False).head()
sns.barplot(x='Protein (g)', y='Food Item', data=top_protein)
plt.title('Top 5 High-Protein Vegetarian Foods')
plt.show()


# Heatmap of correlations
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Heatmap of Nutrients')
plt.show()