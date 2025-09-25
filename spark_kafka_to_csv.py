from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# إنشاء جلسة Spark
spark = SparkSession.builder \
    .appName("KafkaWeatherConsumer") \
    .getOrCreate()

# تقليل مستوى السجلات
spark.sparkContext.setLogLevel("WARN")

# قراءة البيانات من Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "weather_data") \
    .option("startingOffsets", "earliest") \
    .load()

# تحويل القيمة من binary إلى string
weather_df = df.selectExpr("CAST(value AS STRING) as weather_data")

# إضافة طابع زمني لكل رسالة
weather_df = weather_df.withColumn("timestamp", expr("current_timestamp()"))

# حفظ البيانات في ملف CSV بشكل مستمر
query = weather_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "weather_csv_output") \
    .option("checkpointLocation", "weather_csv_checkpoint") \
    .start()

# تشغيل الـ stream حتى يتم إيقافه يدويًا
query.awaitTermination()
