# Student Mental Health Analysis – End-to-End Data Pipeline Project

This project focuses on analyzing student mental health using real-world data and building a complete data pipeline from **Exploratory Data Analysis (EDA)** to **data streaming with Apache Kafka**, storage in **MySQL**, and final reporting using **Power BI**.

## Project Objective

To explore factors affecting student mental health and build a data pipeline that:
- Collects streaming data using Kafka
- Stores data in a structured MySQL database
- Connects to Power BI for live dashboards and visual analytics

---

## Workflow Overview

### 1. **Exploratory Data Analysis (EDA)**
- Analyzed the `student mental health.csv` dataset using Python
- Libraries: `pandas`, `seaborn`, `matplotlib`
- Identified correlations between mental health and features like academic load, parental pressure, sleep patterns, etc.

### 2. **Apache Kafka Setup**
- Created producers and consumers for streaming data:
  - `producer.py`, `producer1.py`, `consumer.py`
- Kafka server and zookeeper configurations (`server.properties`, setup images)
- Topics created to simulate real-time student data flow

### 3. **MySQL Integration**
- Streamed data was pushed into MySQL using connector code (`connectorcode.py`)
- SQL script used for schema creation and data ingestion (`power bi sql connector code.sql`)

### 4. **Power BI Dashboard**
- Connected Power BI to MySQL
- Built interactive visualizations to monitor mental health trends in real-time
- Screenshots: `visualizations on power bi.png`

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `STUDENT_MENTAL_HEALTH_ANALYSIS.ipynb` | Full EDA notebook |
| `student mental health.csv` | Dataset |
| `producer.py`, `consumer.py` | Kafka scripts |
| `connectorcode.py` | MySQL connector script |
| `power bi sql connector code.sql` | SQL schema for Power BI |
| PNG files | Visual references (terminal, Power BI, Kafka setup) |

---

## 🛠️ Tools & Technologies

- **Python** (pandas, seaborn, matplotlib, mysql-connector)
- **Apache Kafka**
- **MySQL**
- **Power BI**
- **Jupyter Notebook**

---

## 📈 Results

- Key influencing factors: academic workload, sleep hours, parental expectations
- Built an automated pipeline to analyze and visualize live student mental health data
- Demonstrated end-to-end integration from raw data to dashboard

---

## How to Run

1. Clone the repository  
2. Install required Python packages (`pip install -r requirements.txt`)  
3. Set up Kafka and Zookeeper  
4. Run producer and consumer scripts  
5. Set up MySQL and execute `.sql` script  
6. Open Power BI and connect to MySQL to view dashboard

---

##  Future Enhancements

- Add sentiment analysis from student survey text
- Integrate Flask-based dashboard as a web app
- Enable alert system for high-risk students

---

##  Certification

This project was completed as part of a data analytics internship and showcases real-time data engineering and visualization skills.

---
