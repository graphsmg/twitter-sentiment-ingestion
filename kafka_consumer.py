import json

from kafka import KafkaConsumer

consumer = KafkaConsumer("test_topic", bootstrap_servers="localhost:9092")

for msg in consumer:
    value = msg.value.decode("utf-8")
    x = json.loads(value)
    print(x["v1"])

