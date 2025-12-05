import pandas as pd

# ==== Load the CSV file ====
df = pd.read_csv(r"C:\Users\ag148\Data_Analysis_Trial\agents.csv.csv")

# ==== Fill missing values with 0 (optional) ====
df.fillna(0, inplace=True)

# ==== Create a composite score to rank agents ====
df['composite_score'] = (
    df['buyer_closes_2024'] * 0.4 +
    df['seller_closes_2024'] * 0.4 +
    df['avg_rating_2024'] * 0.2
)

# ==== Combine first and last name into one column ====
df['full_name'] = df['first_name'] + ' ' + df['last_name']

# ==== Find the best agent per market ====
best_agents = df.loc[df.groupby('market_id')['composite_score'].idxmax()]

# ==== Select relevant columns to show ====
best_agents_result = best_agents[['market_id', 'full_name', 'buyer_closes_2024',
                                  'seller_closes_2024', 'customer_reviews_2024',
                                  'avg_rating_2024', 'composite_score']]

# ==== Display the result ====
print(best_agents_result)

# ==== Save to Excel (.xlsx) ====
best_agents_result.to_excel(r"C:\Users\ag148\Data_Analysis_Trial\best_agents_per_market.xlsx",
                            index=False)
