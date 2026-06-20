import pandas as pd

def load_clean_data(path):
    return pd.read_csv(path)


def add_features(df):

    # occupancy rate (using availability)
    df['occupancy_rate'] = 1 - (df['availability_365'] / 365)

    # estimated annual revenue (simple approximation)
    df['estimated_revenue'] = df['price'] * df['occupancy_rate'] * 365

    # price per bedroom
    df['price_per_bedroom'] = df['price'] / df['bedrooms']

    # host tenure (years)
    df['host_since'] = pd.to_datetime(df['host_since'], errors='coerce')
    df['host_tenure_years'] = (pd.Timestamp.today() - df['host_since']).dt.days / 365

    return df


if __name__ == "__main__":
    df = load_clean_data("data/processed/listings_clean.csv")
    df = add_features(df)

    df.to_csv("data/processed/listings_featured.csv", index=False)

    print("✅ Feature engineering complete.")