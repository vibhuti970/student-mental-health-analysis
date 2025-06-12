from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

data = {
    "Age": 21,
    "Gender": "Female",
    "ScreenTime": 6.5,
    "SleepDuration": 7.5,
    "PhysicalActivity": 5.0,
    "StressLevel": "Medium"
}

producer.send('student-health', data)
producer.flush()
print("Message sent to Kafka topic.")
