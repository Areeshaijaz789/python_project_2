# 🧹 Automated Data Cleaning Script
# Author: Areesha Ijaz
# Project: Task Automation Script (Data Science Internship - CodeAlpha)

import pandas as pd
import numpy as np
import os

# ========== Step 1: Load Dataset ==========
print("🔹 Welcome to the Automated Data Cleaning Script!")
file_path = input("Enter the path of your CSV file: ")

if not os.path.exists(file_path):
    print("❌ File not found! Please check the path and try again.")
    exit()

df = pd.read_csv(file_path)
print("\n✅ Dataset Loaded Successfully!")
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# ========== Step 2: Missing Values Check ==========
print("\n🔹 Checking for Missing Values...")
missing_summary = df.isnull().sum()
print(missing_summary[missing_summary > 0])

# ========== Step 3: Handle Missing Values ==========
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\n✅ Missing Values Handled Successfully!")

# ========== Step 4: Remove Duplicates ==========
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"\n🧾 Removed {before - after} duplicate rows.")

# ========== Step 5: Detect & Handle Outliers (IQR Method) ==========
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_limit) & (df[col] <= upper_limit)]

print("\n✅ Outliers handled successfully using IQR method.")

# ========== Step 6: Summary Report ==========
print("\n📊 Summary Statistics:")
print(df.describe())

# ========== Step 7: Save Cleaned Dataset ==========
output_path = "cleaned_dataset.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Cleaned dataset saved as '{output_path}' in the current directory!")

print("\n🎉 Data Cleaning Completed Successfully!")
print("You can now use 'cleaned_dataset.csv' for further analysis or ML models.")
