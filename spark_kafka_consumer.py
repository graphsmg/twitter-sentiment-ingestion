import time

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

APP_NAME = "KafkaStreamingExample"

sc = SparkContext(master="spark://127.0.0.1:7077", appName=APP_NAME)
ssc = StreamingContext(sc, 1)  # 1 second window

spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

# Subscribe to 1 topic

while True:
    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "127.0.0.1:9092")
        .option("subscribe", "test_topic")
        .load()
    )

    print(df)
    time.sleep(1)
