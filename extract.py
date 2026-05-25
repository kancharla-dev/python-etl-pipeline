import pandas as pd
import logging

def extract_data(path):
    logging.info("Extracting data from CSV...")
    df = pd.read_csv(path)
    logging.info(f"Rows extracted: {len(df)}")
    return df
