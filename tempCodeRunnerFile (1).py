mport pandas as pd
import mysql.connector

# 1. Load the cleaned CSV (make sure it's in the same folder or give full path)
df = pd.read_csv("student mental health.csv")

# 2. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vibhuti@2114",      # Use your MySQL password
    database="student_health"     # Make sure this database already exists
)

cursor = conn.cursor()

# Create table with correct column names
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Age INT,
    Gender VARCHAR(10),
    `Screen Time (hrs/day)` FLOAT,
    `Sleep Duration (hrs)` FLOAT,
    `Physical Activity (hrs/week)` FLOAT,
    `Stress Level` VARCHAR(10)
)
""")

# Insert rows into table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO student_data (
            Age, Gender, `Screen Time (hrs/day)`, `Sleep Duration (hrs)`,
            `Physical Activity (hrs/week)`, `Stress Level`
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['Age'],
        row['Gender'],
        row['Screen Time (hrs/day)'],
        row['Sleep Duration (hrs)'],
        row['Physical Activity (hrs/week)'],
        row['Stress Level']
    ))


# 5. Commit the transaction and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully into MySQL.")
