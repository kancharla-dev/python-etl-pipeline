import logging
logging.basicConfig(filename="logs/pipeline.log", level=logging.INFO, format="%(asctime)s - %(message)s")

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def main():
    df = extract_data("data/raw.csv")
    df_clean = transform_data(df)
    load_data(df_clean, "output/netflix.db")

if __name__ == "__main__":
    main()
