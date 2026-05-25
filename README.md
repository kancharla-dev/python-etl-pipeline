# Python ETL Pipeline (Netflix Dataset)

A simple and clean **ETL (Extract → Transform → Load)** pipeline built using Python.  
This project processes the **Netflix Movies and TV Shows Dataset** from Kaggle and loads the cleaned data into a SQLite database.

---

##  Project Overview

This project demonstrates a real-world style ETL workflow:

### 1️⃣ Extract  
Reads the raw Netflix dataset (`raw.csv`) from the `data/` folder.

### 2️⃣ Transform  
Cleans and prepares the dataset by:
- Removing duplicate records  
- Dropping rows missing essential fields (title, type)  
- Filling other missing values with `"Unknown"`  

### 3️⃣ Load  
Stores the cleaned dataset into a SQLite database (`netflix.db`) inside the `output/` folder.

---

## 🗂️ Project Structure
python-etl-pipeline/
├── src/
│     ├── extract.py
│     ├── transform.py
│     └── load.py
├── data/
│     └── raw.csv
├── output/
│     └── netflix.db
├── logs/
│     └── pipeline.log
├── main.py
├── requirements.txt
└── README.md


---

##  How It Works

###  `main.py`
Coordinates the entire ETL pipeline.

###  `extract.py`
Loads the CSV file using pandas.

###  `transform.py`
Cleans and prepares the dataset.

###  `load.py`
Writes the cleaned data into a SQLite database.

---

##  How to Run the Pipeline

### 1. Install dependencies

### 2. Run the ETL pipeline

### 3. Output
A SQLite database will be created at:output/netflix.db

---

##  Dataset Source

Netflix Movies and TV Shows Dataset  
Source: Kaggle (public dataset)

---

##  Tech Stack

- Python  
- Pandas  
- SQLite  
- VS Code  

---

##  Future Enhancements

- Add Airflow scheduling  
- Add dbt transformations  
- Add Power BI dashboard  
- Add API ingestion  
- Add unit tests  

---

##  Author

** kavitha Kancharla**  
Aspiring Data Engineer | Finland  




