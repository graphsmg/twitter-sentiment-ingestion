import json
import pprint

from kafka import KafkaConsumer

consumer = KafkaConsumer("recent_tweets_downloader", bootstrap_servers="localhost:9092")

for msg in consumer:
    value = msg.value.decode("utf-8")
    x = json.loads(value)
    pprint.pprint(x)

