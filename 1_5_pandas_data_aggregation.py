import pandas as pd

# Group data by 'Category' and calculate the mean of 'Value'
data = {"Category": ["A", "B", "A", "B", "A", "B"], "Value": [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)
grouped = df.groupby("Category")["Value"].mean()
print("Grouped data:", grouped)

# Aggregate data using multiple functions
aggregated = df.groupby("Category")["Value"].agg(["mean", "sum", "count"])
print("Aggregated data:", aggregated)


# Aggregate data with custom functions
def custom_agg(x):
    return x.max() - x.min()


custom_aggregated = df.groupby("Category")["Value"].agg(custom_agg)
print("Custom aggregated data:", custom_aggregated)

# Pivot table to summarize data
pivot_table = df.pivot_table(values="Value", index="Category", aggfunc="mean")
print("Pivot table:", pivot_table)
