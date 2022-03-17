import time
import json
import pprint

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

APP_NAME = "KafkaStreamingExample"

sc = SparkContext(master="spark://127.0.0.1:7077", appName=APP_NAME)
ssc = StreamingContext(sc, 1)  # 1 second window

spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

# Subscribe to 1 topic

while True:
    # Cannot get to work, writestream error
    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "127.0.0.1:9092")
        .option("subscribe", "recent_tweets_downloader")
        .load()
    )

    # print(type(df))
    # print(dir(df))
    # break

    print(df.tail(5))
    # print(dir(df))
    # print(df.writeStream.start())
    # print(df.head())
    time.sleep(1)
