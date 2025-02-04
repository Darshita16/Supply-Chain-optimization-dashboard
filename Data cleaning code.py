# Remove duplicates
data_cleaned = data.drop_duplicates()

# Standardize column names
data_cleaned.columns = data_cleaned.columns.str.strip().str.replace(' ', '_').str.lower()

# Convert categorical columns to consistent formats
categorical_cols = ['product_type', 'customer_demographics', 'shipping_carriers', 'inspection_results']
for col in categorical_cols:
    data_cleaned[col] = data_cleaned[col].str.strip().str.capitalize()

# Check and handle outliers in numerical columns (example: 'defect_rates')
for col in ['price', 'revenue_generated', 'defect_rates', 'costs']:
    q1 = data_cleaned[col].quantile(0.25)
    q3 = data_cleaned[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    data_cleaned = data_cleaned[(data_cleaned[col] >= lower_bound) & (data_cleaned[col] <= upper_bound)]

# Drop irrelevant columns (if any)
# data_cleaned = data_cleaned.drop(['unnecessary_column'], axis=1)

# Save the cleaned dataset
output_path = '/mnt/data/supply_chain_data_cleaned.csv'
data_cleaned.to_csv(output_path, index=False)

output_path
