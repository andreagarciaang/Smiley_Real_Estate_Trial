import pandas as pd
import os

# --- Step 1: CSV path ---
input_csv = r"C:\Users\ag148\Data_Analysis_Trial\markets.csv.csv"
output_csv = r"C:\Users\ag148\Data_Analysis_Trial\best_market_results.csv"

# --- Step 2: Load CSV ---
df = pd.read_csv(input_csv)
print("CSV loaded successfully!\n")

# --- Step 3: Ensure necessary columns exist ---
required_columns = ['market_id', 'listings_closed_count', 'population', 'price_closed_median']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"CSV must contain '{col}' column")

# --- Step 4: Normalize the metrics (0-1 scale) ---
df['activity_score'] = df['listings_closed_count'] / df['listings_closed_count'].max()
df['population_score'] = df['population'] / df['population'].max()
df['price_score'] = df['price_closed_median'] / df['price_closed_median'].max()

# --- Step 5: Compute composite score ---
df['composite_score'] = (df['activity_score'] + df['population_score'] + df['price_score']) / 3

# --- Step 6: Rank markets by composite score ---
best_markets = df.sort_values(by='composite_score', ascending=False)

# --- Step 7: Keep only relevant columns for output ---
output_columns = ['market_id', 'listings_closed_count', 'population', 'price_closed_median', 'composite_score']
top_markets = best_markets[output_columns].head(10)

# --- Step 8: Save top 10 markets to CSV ---
top_markets.to_csv(output_csv, index=False)
print(f"Top 10 markets saved to CSV: {output_csv}")

# --- Step 9: Open the CSV automatically in Excel ---
os.startfile(output_csv)
