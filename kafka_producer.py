import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(100):
    x = json.dumps({"v1": 1, "v2": 2})
    r = producer.send(topic="test_topic", value=bytes(x, "utf-8"))
    print(r.is_done)

