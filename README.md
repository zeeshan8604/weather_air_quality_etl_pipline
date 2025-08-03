# Weather & Air Quality ETL Pipeline

This project is an end-to-end **ETL (Extract, Transform, Load) pipeline** that gathers weather and air quality data from public APIs, cleans and merges the datasets, and loads them into a PostgreSQL database. It also includes basic data analysis and visualization using Jupyter Notebook.

## 🚀 Features

- 📥 **Data Extraction** from Visual Crossing (Weather API) and AirVisual (Air Quality API)
- 🧹 **Data Transformation** using Pandas (cleaning, merging, formatting)
- 🛢️ **Data Loading** into PostgreSQL using SQLAlchemy
- 📊 **Exploratory Data Analysis** in Jupyter Notebook
- 🗂️ Configurable API keys and endpoints via environment variables

## 🔧 Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Jupyter Notebook
- APIs: Visual Crossing & AirVisual

## 🧠 Skills Demonstrated

- Real-world ETL architecture
- API integration and error handling
- Data cleaning and transformation
- Relational database usage for analytics
- Modular Python scripting

## 📈 Sample Output

- Cleaned and structured weather + AQI data
- EDA charts showing temperature vs AQI
- PostgreSQL tables for structured querying

## 📁 Project Structure

── extract/ # Scripts to fetch data from APIs
├── transform/ # Scripts to clean and merge datasets
├── load/ # PostgreSQL loader scripts
├── notebooks/ # Jupyter Notebook for analysis
├── requirements.txt # Python dependencies
├── .env # API keys and credentials (not pushed)
└── README.md

## 📌 Note

This project is a customized and enhanced version of an open-source pipeline originally created by [@themispap](https://github.com/themispap).

## 👤 Author

**Zeeshan Ahmed**  
[GitHub Profile](https://github.com/zeeshan8604)
