from kafka import KafkaProducer
import time
import random

# إعداد المنتج
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: x.encode('utf-8')
)

print("🚀 بدأ إرسال بيانات الطقس إلى Kafka...")

while True:
    temperature = round(random.uniform(15, 45), 1)
    humidity = random.randint(20, 100)
    wind_speed = round(random.uniform(0, 20), 1)
    message = f"Temp={temperature}°C, Humidity={humidity}%, Wind={wind_speed}km/h"

    producer.send('weather_data', value=message)
    print(f"✅ أُرسلت: {message}")
    time.sleep(5)  # كل 5 ثواني
