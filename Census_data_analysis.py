import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv('census_income_dataset.csv')

#Age distribution(Plot 1)
plt.figure(figsize=(10, 8))
plt.hist(df['AGE'], bins=20, color='mediumseagreen')
plt.title('Age distribution of respondents', fontsize=14)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add a light grid for better readability
plt.show()


#Relationship status frequency(Plot 2)
plt.figure(figsize=(10, 8))
df['RELATIONSHIP'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90)
plt.title('Relationship status', fontsize=14)
plt.ylabel('')  #Removes the y-label for a cleaner look
plt.show()



#Respondents' Salary (<=50k or >50k) by Educational Level (Plot 3)
df['SALARY_GROUP'] = df['SALARY'].apply(lambda x: 0 if x.strip() == '<=50K' else 1)  # Group salary
education_salary = df.groupby(['EDUCATION', 'SALARY_GROUP']).size().unstack(fill_value=0)

#Stacked Bar Chart
education_salary.plot(kind='bar', stacked=True, figsize=(10, 8), color=["red", "blue"])
plt.title("Educational level and salary", fontsize=14)
plt.xlabel("Education Level", fontsize=11)
plt.ylabel("Count", fontsize=14)
plt.xticks(rotation=30, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(['<=50K', '>50K'], title="Salary", fontsize=14)
plt.show()
