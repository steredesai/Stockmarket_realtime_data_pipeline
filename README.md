# Stockmarket_realtime_data_pipeline

This repository contains two Python scripts designed to work together to fetch, produce, and consume real-time stock market data using Apache Kafka.

## Features
- **Producer**: Fetches real-time stock data using the Alpha Vantage API and publishes it to a Kafka topic.
- **Consumer**: Consumes stock market data from the Kafka topic and writes it to a JSON file.

## Prerequisites

Before using these scripts, ensure you have the following:
- Python 3.7 or higher
- Kafka installed and running locally
- An Alpha Vantage API key

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-market-kafka.git
   cd stock-market-kafka
   ```

2. Install the required Python dependencies:
   ```bash
   pip install confluent-kafka requests
   ```

3. Set up your Kafka broker. Ensure Kafka is running on `localhost:9092`, or update the broker configuration in the scripts if necessary.

4. Obtain an Alpha Vantage API key by signing up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

## Usage

### Producer Script

1. Open the `producer.py` file and set the following variables:
   - `API_KEY`: Your Alpha Vantage API key.
   - `SYMBOL`: The stock symbol you wish to track (e.g., TSLA).
   - `BROKER`: Kafka broker address (default: `localhost:9092`).

2. Run the producer script:
   ```bash
   python producer.py
   ```

   The script fetches stock data at 1-minute intervals and streams it to the Kafka topic `stock_market_data`.

### Consumer Script

1. Open the `consumer.py` file and verify the following:
   - `KAFKA_TOPIC`: The Kafka topic to consume data from (default: `stock_market_data`).
   - `BROKER`: Kafka broker address (default: `localhost:9092`).
   - `OUTPUT_FILE`: Path to the output JSON file (default: `stock_market_data_output.json`).

2. Run the consumer script:
   ```bash
   python consumer.py
   ```

   The script listens to the Kafka topic and writes the received messages to the specified JSON file.

## Configuration

- **Kafka Broker**: Update the `BROKER` variable in both scripts if your Kafka instance is not running locally.
- **Kafka Topic**: Change the `KAFKA_TOPIC` variable in both scripts to use a different topic.
- **Output File**: Modify the `OUTPUT_FILE` variable in the consumer script to specify a custom output file path.

## Troubleshooting

- Ensure Kafka is running before starting the producer or consumer scripts.
- Check that your API key is valid and has not exceeded the rate limit.
- If there are connection issues, verify the broker address and ensure your Kafka instance is accessible.



