import pandas as pd
import mysql.connector

df = pd.read_csv("student mental health.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vibhuti@2114",  
    database="student_health"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO student_data (
            Age, Gender, ScreenTime, SleepDuration, PhysicalActivity, StressLevel
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        int(row['Age']),
        row['Gender'],
        float(row['Screen Time (hrs/day)']),
        float(row['Sleep Duration (hrs)']),
        float(row['Physical Activity (hrs/week)']),
        row['Stress Level']
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully into MySQL.")
