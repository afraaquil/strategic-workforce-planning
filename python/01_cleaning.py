import pandas as pd
import numpy as np

# Load IBM dataset
ibm_df = pd.read_csv('/Users/afraaquil/Desktop/minor project/ibm_clean.csv')

# Load performance dataset
perf_df = pd.read_csv('/Users/afraaquil/Desktop/minor project/hr perfomance.csv')

# Check shapes
print("IBM shape:", ibm_df.shape)
print("Performance shape:", perf_df.shape)
print("\nIBM columns:", list(ibm_df.columns))

# Merge both datasets on EmployeeNumber
df = pd.merge(ibm_df, perf_df, on='EmployeeNumber')
# Fix duplicate column names after merge
df = df.drop(columns=['Department_y'])
df = df.rename(columns={'Department_x': 'Department'})

print("\nMerged shape:", df.shape)
print("Merge successful!")

# Drop columns we don't need
df = df.drop(columns=['EmployeeCount', 'StandardHours', 'Over18'])

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing numbers with median
df.fillna(df.median(numeric_only=True), inplace=True)

print("\nAfter cleaning shape:", df.shape)
# Feature Engineering — create new columns from existing ones
df['workload_ratio'] = df['TasksCompleted'] / df['ContractHours']

df['tenure_band'] = pd.cut(df['YearsAtCompany'],
    bins=[0, 2, 5, 10, 100],
    labels=['0-2yr', '3-5yr', '6-10yr', '10+yr'])

print("\nNew columns added!")
print("Workload ratio sample:", df['workload_ratio'].head())
print("\nTenure band counts:")
print(df['tenure_band'].value_counts())
# Save cleaned file
df.to_csv('/Users/afraaquil/Desktop/minor project/workforce_clean.csv', index=False)

print("\n✅ workforce_clean.csv saved successfully!")
print("Final shape:", df.shape)