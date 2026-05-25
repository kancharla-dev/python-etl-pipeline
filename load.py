import sqlite3
import logging

def load_data(df, db_path):
    logging.info("Loading data into SQLite database...")

    conn = sqlite3.connect(db_path)
    df.to_sql("netflix_titles", conn, if_exists="replace", index=False)
    conn.close()

    logging.info("Data loaded successfully!")
