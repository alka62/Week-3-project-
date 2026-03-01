# Step 1: Import required library
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv("sales_data.csv")

print("Dataset Loaded Successfully!\n")

# Step 3: Basic Information
print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Shape (Rows, Columns):")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Step 4: Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values if any
df = df.fillna(0)

# Step 5: Calculate Total Revenue
total_revenue = df["Total_Sales"].sum()
print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

# Step 6: Find Best Selling Product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
best_product_sales = df.groupby("Product")["Total_Sales"].sum().max()

print(f"\nBest Selling Product: {best_product}")
print(f"Sales of Best Product: ₹{best_product_sales:,.2f}")

# Step 7: Additional Metrics
average_sales = df["Total_Sales"].mean()
max_sale = df["Total_Sales"].max()
min_sale = df["Total_Sales"].min()

print(f"\nAverage Sale: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{max_sale:,.2f}")
print(f"Lowest Single Sale: ₹{min_sale:,.2f}")

print("\nAnalysis Completed Successfully!")
