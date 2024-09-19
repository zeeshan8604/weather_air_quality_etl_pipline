# **Weather and Air Quality ETL Pipeline**

## **Project Overview**

This project demonstrates an ETL (Extract, Transform, Load) pipeline that integrates weather and air quality data for a specified city over a defined time period. The data is extracted from external APIs, transformed (cleaned and processed), and loaded into a PostgreSQL database. The goal of this project is to provide a clean, well-structured dataset for further analysis or reporting.

## **Project Structure**
```
├── src
│   ├── extract.py        # Code for extracting data from APIs
│   ├── transform.py      # Code for cleaning and transforming the data
│   ├── load.py           # Code for loading data into PostgreSQL
│   ├── config.py         # Configuration for API keys, database credentials
│   └── utils.py          # Utility functions for the ETL process
├── sql
│   └── schema.sql        # SQL script for creating database schema
├── notebooks
│   └── analysis.ipynb    # Jupyter notebook for data exploration and analysis
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## **Technologies Used**
- **Programming Language:** Python
- **Database:** PostgreSQL
- **Data Sources:**
  - **Weather API:** [OpenWeather](https://openweathermap.org/api)
  - **Air Quality API:** [OpenAQ](https://openaq.org/#/)

- **Python Libraries:**
  - `requests`: For interacting with APIs.
  - `pandas`: For data manipulation and cleaning.
  - `SQLAlchemy`/`psycopg2`: For database interaction.
  - `numpy`: For numerical computations.
  - `dotenv`: To handle environment variables (API keys, DB credentials).

## **ETL Pipeline Breakdown**

### **1. Data Extraction**
- **Weather Data:** Collected using the OpenWeather API. Data includes temperature, humidity, wind speed, and weather conditions.
- **Air Quality Data:** Collected using the OpenAQ API, which provides air quality measurements such as PM2.5, PM10, and AQI (Air Quality Index).
  
### **2. Data Transformation**
- Handle missing data and clean the dataset.
- Convert temperature units (Kelvin to Celsius).
- Merge weather and air quality datasets based on date and location.
- Create additional features such as "Feels like temperature" or AQI categories (Good, Moderate, Unhealthy, etc.).

### **3. Data Loading**
- Store the cleaned and transformed data into a PostgreSQL database.
- Database schema includes separate tables for **weather**, **air quality**, and **merged data**.

### **4. Data Analysis (Optional)**
- Basic exploratory analysis using SQL queries or in a Jupyter notebook.
- Queries include:
  - Average daily temperature and air quality.
  - Correlation analysis between weather and air quality metrics.

## **How to Run the Project**

### **1. Prerequisites**
- **Python** (version 3.7 or above)
- **PostgreSQL** (with database and user access)
- API keys for [OpenWeather](https://openweathermap.org/api) and [OpenAQ](https://openaq.org/#/)

### **2. Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/weather-air-quality-etl.git
   cd weather-air-quality-etl
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the root directory with the following keys:
     ```
     OPENWEATHER_API_KEY=<your_openweather_api_key>
     OPENAQ_API_KEY=<your_openaq_api_key>
     DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
     ```

5. Set up the PostgreSQL database:
   - Run the SQL script to create the schema:
     ```bash
     psql -U <username> -d <dbname> -f sql/schema.sql
     ```

6. Run the ETL pipeline:
   ```bash
   python src/extract.py
   python src/transform.py
   python src/load.py
   ```

### **3. Running Analysis**
- Explore the data using the provided Jupyter notebook:
  ```bash
  jupyter notebook notebooks/analysis.ipynb
  ```

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
