import pandas as pd
import numpy as np

df = pd.read_csv('supply_chain_data.csv')

# 1. Initial exploration
print("Dataset shape:", df.shape)
print("\nColumn names and types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nFirst few rows:")
print(df.head())

# 2. Data cleaning
# Convert date columns to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Check for any negative values in numeric columns (data quality)
numeric_cols = ['Base_Lead_Time_Days', 'Actual_Lead_Time_Days', 
                'Delay_Days', 'Shipping_Cost_USD', 
                'Geopolitical_Risk_Index', 'Weather_Severity_Index']

for col in numeric_cols:
    if (df[col] < 0).any():
        print(f"Warning: Negative values found in {col}")

# 3. Create additional calculated columns

# Delivery efficiency (%)
df['On_Time_Flag'] = np.where(df['Delivery_Status'] == 'On Time', 1, 0)

# Cost per day
df['Cost_Per_Day'] = df['Shipping_Cost_USD'] / df['Actual_Lead_Time_Days']

# Risk category (bucketing for easier analysis)
df['Risk_Level'] = pd.cut(df['Geopolitical_Risk_Index'], 
                          bins=[0, 0.3, 0.6, 1.0],
                          labels=['Low', 'Medium', 'High'])

# Quarter and Month extraction
df['Order_Quarter'] = df['Order_Date'].dt.to_period('Q').astype(str)
df['Order_Month'] = df['Order_Date'].dt.month
df['Order_Year'] = df['Order_Date'].dt.year

# 4. Create lookup tables (for star schema)

# Dimension: Routes
dim_routes = df[['Route_Type', 'Origin_City', 'Destination_City']].drop_duplicates()
dim_routes['Route_ID'] = range(1, len(dim_routes) + 1)

# Dimension: Products
dim_products = df[['Product_Category']].drop_duplicates()
dim_products['Product_ID'] = range(1, len(dim_products) + 1)

# Dimension: Disruptions
dim_disruptions = df[['Disruption_Event']].drop_duplicates()
dim_disruptions['Disruption_ID'] = range(1, len(dim_disruptions) + 1)

# Merge IDs back to main fact table
df = df.merge(dim_routes, on=['Route_Type', 'Origin_City', 'Destination_City'], how='left')
df = df.merge(dim_products, on='Product_Category', how='left')
df = df.merge(dim_disruptions, on='Disruption_Event', how='left')

# 5. Save cleaned files
df.to_csv('fact_shipments.csv', index=False)
dim_routes.to_csv('dim_routes.csv', index=False)
dim_products.to_csv('dim_products.csv', index=False)
dim_disruptions.to_csv('dim_disruptions.csv', index=False)

print("\nData cleaning complete! Files saved:")
print("- fact_shipments.csv")
print("- dim_routes.csv")
print("- dim_products.csv")
print("- dim_disruptions.csv")