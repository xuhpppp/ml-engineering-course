import pandas as pd

# Drop rows and columns with missing values
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', None]
})
print("Original DataFrame:\n", df)
df_row_dropped = df.dropna()
df_col_dropped = df.dropna(axis=1)
print("\nDataFrame after dropping rows with missing values:\n", df_row_dropped)
print("\nDataFrame after dropping columns with missing values:\n", df_col_dropped)

# Fill missing values with a specific value
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'})
print("\nDataFrame after filling missing values:\n", df_filled)

# ffill and bfill methods
df_ffill = df.ffill()
df_bfill = df.bfill()
print("\nDataFrame after forward filling missing values:\n", df_ffill)
print("\nDataFrame after backward filling missing values:\n", df_bfill)

# Interpolate missing values on numeric DataFrame
df_numeric = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [None, 1, 2, None, 5]
})
df_interpolated = df_numeric.interpolate()
print("\nOriginal numeric DataFrame:\n", df_numeric)
print("\nDataFrame after interpolation:\n", df_interpolated)

# Rename columns
df_renamed = df.rename(columns={'Name': 'Full Name', 'Age': 'Years', 'City': 'Location'})
print("\nDataFrame after renaming columns:\n", df_renamed)

# Change data types
df['Age'] = df['Age'].astype('float')
print("\nDataFrame after changing data type of 'Age' to float:\n", df)

# Modify values in a column
df['Age'] = df['Age'] + 1
print("\nDataFrame after adding 1 to 'Age' column:\n", df)

# Combine and merge DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Age': [25, 30, 35]
})
df_combined = pd.merge(df1, df2, on='ID', how='outer')
print("\nMerged DataFrame:\n", df_combined)
df_concatenated = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nConcatenated DataFrame:\n", df_concatenated)