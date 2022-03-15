from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(100):
    r = producer.send(topic="test_topic", value=b"abc")
    print(r.is_done)

