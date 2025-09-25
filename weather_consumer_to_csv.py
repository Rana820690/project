from kafka import KafkaConsumer
import csv
from datetime import datetime

# إعداد المستهلك
consumer = KafkaConsumer(
    'weather_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='weather-group',
    value_deserializer=lambda x: x.decode('utf-8')
)

# فتح ملف CSV للحفظ
filename = f"weather_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Weather Data"])

    print(f"📁 يتم حفظ البيانات في: {filename}")

    for message in consumer:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, message.value])
        print(f"💾 حفظ: {message.value}")
