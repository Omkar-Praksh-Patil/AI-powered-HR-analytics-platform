import pandas as pd

# Load original dataset (check exact file name)
df = pd.read_csv("employee_data.csv")

# Select important columns
df = df[['Age', 'TotalWorkingYears', 'MonthlyIncome', 'JobSatisfaction', 'Attrition']]

# Convert target variable
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Remove missing values (if any)
df = df.dropna()

# Save cleaned dataset
df.to_csv("employee_cleaned.csv", index=False)

print("Cleaned dataset created successfully ")
print(df.head())