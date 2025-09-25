import random
import csv
import time
from datetime import datetime

print("يتم الآن إنشاء ملف جديد كل 5 ثواني... اضغط Ctrl+C للإيقاف.")

try:
    while True:
        # توليد بيانات الطقس
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(15, 45), 1)
        humidity = random.randint(20, 100)
        wind_speed = round(random.uniform(0, 20), 1)

        # اسم الملف بناءً على الوقت
        filename = f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        # حفظ البيانات في ملف جديد
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)"])
            writer.writerow([timestamp, temperature, humidity, wind_speed])

        print(f"📁 تم إنشاء الملف: {filename}")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 تم إيقاف إنشاء الملفات.")

