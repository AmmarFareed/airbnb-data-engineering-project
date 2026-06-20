import pandas as pd

# -----------------------------
# Load data
# -----------------------------
def load_listings(path):
    return pd.read_csv(path)


# -----------------------------
# Clean price column
# -----------------------------
def clean_price(df):
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    return df


# -----------------------------
# Drop unnecessary columns
# -----------------------------
def drop_columns(df):
    cols_to_drop = [
        'license',
        'calendar_updated',
        'neighbourhood_group_cleansed'
    ]
    df = df.drop(columns=cols_to_drop)
    return df


# -----------------------------
# Handle missing values
# -----------------------------

def handle_missing(df):
    df['beds'] = df['beds'].fillna(df['beds'].median())
    df['bathrooms'] = df['bathrooms'].fillna(df['bathrooms'].median())
    df['review_scores_rating'] = df['review_scores_rating'].fillna(0)

    df = df.dropna(subset=['price'])

    return df



# -----------------------------
# Run full cleaning pipeline
# -----------------------------
def clean_listings(path):
    df = load_listings(path)
    df = clean_price(df)
    df = drop_columns(df)
    df = handle_missing(df)
    return df


# -----------------------------
# Save cleaned data
# -----------------------------
if __name__ == "__main__":
    df = clean_listings("data/raw/listings.csv.gz")
    df.to_csv("data/processed/listings_clean.csv", index=False)

    print("✅ Cleaning complete. File saved.")