from confluent_kafka import Producer
import json
import requests
import time

# Configuration
API_URL = "https://www.alphavantage.co/query"
API_KEY = ""  # Your Alpha Vantage API key
SYMBOL = "TSLA"  # Tesla stock symbol
KAFKA_TOPIC = "stock_market_data"
BROKER = "localhost:9092"  # Kafka broker

# Initialize Kafka Producer
producer_config = {
    "bootstrap.servers": BROKER
}
producer = Producer(producer_config)


def fetch_stock_data():
    """
    Fetches real-time stock data from the Alpha Vantage API.
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": SYMBOL,
        "interval": "1min",
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("Time Series (1min)", {})
    else:
        print(f"Error fetching stock data: {response.status_code}")
        return {}


# Stream stock data to Kafka
while True:
    stock_data = fetch_stock_data()
    if stock_data:
        for timestamp, values in stock_data.items():
            message = {
                "symbol": SYMBOL,
                "timestamp": timestamp,
                "data": values
            }
            producer.produce(KAFKA_TOPIC, key=SYMBOL, value=json.dumps(message))
            print(f"Sent: {message}")
        producer.flush()
    else:
        print("No stock data fetched this time.")

    # Fetch data every minute
    time.sleep(60)
