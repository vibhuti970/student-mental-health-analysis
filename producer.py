import csv
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('student mental health.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        producer.send('student-mental-health', value=row)
        print(f"Sent: {row}")

producer.flush()
producer.close()
