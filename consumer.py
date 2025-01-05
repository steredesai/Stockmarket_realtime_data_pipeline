from confluent_kafka import Consumer, KafkaException
import json

KAFKA_TOPIC = "stock_market_data"
BROKER = "localhost:9092"
OUTPUT_FILE = "stock_market_data_output.json"  # Output file path

# Initialize Kafka Consumer
consumer_config = {
    "bootstrap.servers": BROKER,
    "group.id": "stock_market_consumer",
    "auto.offset.reset": "earliest"
}
consumer = Consumer(consumer_config)
consumer.subscribe([KAFKA_TOPIC])

print("Listening for stock market data and writing to file...")

try:
    with open(OUTPUT_FILE, "a") as file:  # Open file in append mode
        while True:
            message = consumer.poll(1.0)  # Timeout of 1 second
            if message is None:
                continue
            if message.error():
                raise KafkaException(message.error())
            else:
                stock_data = json.loads(message.value().decode('utf-8'))
                print(f"Received: {stock_data}")
                # Write message to file
                file.write(json.dumps(stock_data) + "\n")
except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    consumer.close()
