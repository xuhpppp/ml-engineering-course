import pandas as pd

# Create a Series from a list
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("Series:\n", s)

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Load data from CSV and Excel files
df_csv = pd.read_csv('files/data.csv')
# df_excel = pd.read_excel('files/data.xlsx')
print("\nDataFrame from CSV:\n", df_csv)
# print("\nDataFrame from Excel:\n", df_excel)

# Save DataFrame to CSV and Excel files
# df.to_csv('files/output.csv', index=False)
# df.to_excel('files/output.xlsx', index=False)

# Viewing DataFrame
print("\nFirst 5 rows of DataFrame:\n", df.head())
print("\nLast 3 rows of DataFrame:\n", df.tail(3))
print("\nDataFrame Info:\n", df.info())
print("\nDataFrame Description:\n", df.describe())

# Selecting columns and rows
print("\nSelect 'Name' and 'Age' columns:\n", df[['Name', 'Age']])

# Select rows where Age > 30
print("\nRows where Age > 30:\n", df[df['Age'] > 30])

# Indexing with loc and iloc
# loc uses label-based indexing, while iloc uses integer-based indexing
print("\nSelect row with index 1 using loc:\n", df.loc[1])
print("\nSelect row with index 1 using iloc:\n", df.iloc[1])
