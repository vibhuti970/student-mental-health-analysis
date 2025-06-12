host="localhost",
    user="root",            # change if needed
    password="Vibhuti@2114",            # change if needed
    database="student_health"
)
cursor = conn.cursor()

# ✅ Kafka topic must match what's being sent from your producer
consumer = KafkaConsumer(
    'student-health',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consuming messages and storing in MySQL...")

for message in consumer:
    data = message.value

    # ✅ Expected fields based on your MySQL table
    try:
        cursor.execute("""
            INSERT INTO student_data (Age, Gender, ScreenTime, SleepDuration, PhysicalActivity, StressLevel)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            int(data.get('Age', 0)),
            data.get('Gender', 'Unknown'),
            float(data.get('ScreenTime', 0)),
            float(data.get('SleepDuration', 0)),
            float(data.get('PhysicalActivity', 0)),
            data.get('StressLevel', 'Unknown')
        ))
        conn.commit()
        print("Inserted:", data)

    except Exception as e:
        print("Error inserting data:", e)
        continue

# Cleanup
cursor.close()
conn.close()
