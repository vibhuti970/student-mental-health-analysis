import json
import mysql.connector
from kafka import KafkaConsumer

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vibhuti@2114",
    database="student_health"
)
cursor = conn.cursor()

consumer = KafkaConsumer(
    'student-health',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='student-group'
)

print("✅ Kafka Consumer is running...")

for message in consumer:
    print("📥 Received message:", message.value)
    data = message.value

    try:
        insert_query = """
        INSERT INTO student_mental_health (age, gender, physicalactivity, screentime, sleepduration, stresslevel)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data.get("Age"),
            data.get("Gender"),
            data.get("PhysicalActivity"),
            data.get("ScreenTime"),
            data.get("SleepDuration"),
            data.get("StressLevel")
        )

        print("➡️ Inserting data:", values)
        cursor.execute(insert_query, values)
        conn.commit()
        print("✅ Inserted successfully.")

        cursor.execute("SELECT * FROM student_mental_health ORDER BY id DESC LIMIT 1")
        latest = cursor.fetchone()
        print("🧾 Latest in DB:", latest)

    except Exception as e:
        print("❌ Error inserting data:", e)

cursor.close()
conn.close()
