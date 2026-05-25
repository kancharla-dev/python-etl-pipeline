import logging

def transform_data(df):
    logging.info("Cleaning data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with missing title or type
    df = df.dropna(subset=["title", "type"])

    # Fill missing values for other columns
    df = df.fillna("Unknown")

    logging.info(f"Rows after cleaning: {len(df)}")
    return df
