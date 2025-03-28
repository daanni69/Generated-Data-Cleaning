import pandas as pd

df = pd.read_csv(r'C:\Users\AB-TECH\Pandas\employee_data.csv', encoding='utf-8')
print(df.head())

#Fill missing Age values with the median age
print(df['Age'].isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'].isnull().sum())

# #Row with missing Salary values
print(df['Salary'].isnull().sum())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
print(df['Salary'].isnull().sum())

# Remove extra spaces from the 'Name' column
if 'Name' in df.columns:
    df['Name'] = df['Name'].str.strip()

# Standardize the 'Department' column to lowercase
if 'Department' in df.columns:
    df['Department'] = df['Department'].str.lower()

# Check for negative values in the 'Salary' column
if 'Salary' in df.columns:  # Ensure the column exists
    negative_values = df[df['Salary'] < 0]
    print("Rows with negative Salary values:")
    print(negative_values)

# Replace negative Salary values with 0
if 'Salary' in df.columns:  # Ensure the column exists
    df['Salary'] = df['Salary'].apply(lambda x: max(x, 0))

negative_count = (df['Salary'] < 0).sum()
print(f"Number of negative Salary values: {negative_count}")

# Check for invalid values in the 'Joining_Date' column
invalid_dates = pd.to_datetime(df['Joining_Date'], errors='coerce').isna()
print("Rows with invalid Joining_Date values:")
print(df[invalid_dates])


# Convert the 'Joining_Date' column to the 'YYYY-MM-DD' format
if 'Joining_Date' in df.columns:  # Ensure the column exists
    df['Joining_Date'] = pd.to_datetime(df['Joining_Date'], errors='coerce').dt.strftime('%Y-%m-%d')


# Check for duplicate rows
duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_count}")

df.to_csv(r'C:\Users\AB-TECH\Pandas\cleaned_employee_data.csv', index=False, encoding='utf-8')
print("\nCleaned dataset saved successfully!")

