# Stock Market Data Streaming with Kafka, Snowflake, and Power BI

This project demonstrates a Kafka-based system for streaming stock market data, which is then loaded into Snowflake for analytics. Finally, Power BI is used to visualize the stock market data for business intelligence and decision-making.

## Components
- **Producer**: Fetches real-time stock data from the Alpha Vantage API and streams it to a Kafka topic.
- **Consumer**: Consumes the stock market data from the Kafka topic and writes it to a JSON file.
- **Visualization**: Uses Power BI to connect to Snowflake and visualize the stock market data.

## Requirements

- Python 3.6 or later
- Kafka (locally or on a cloud instance)
- Snowflake account
- Power BI Desktop
- Alpha Vantage API key for accessing stock data

### Required Python libraries:

- `confluent_kafka`
- `requests`
- `json`

Install the required libraries with pip:

```bash
pip install confluent_kafka requests
```

## Setup

### 1. Install Kafka
If you don’t have Kafka installed locally, you can follow the [Kafka installation guide](https://kafka.apache.org/quickstart) for setting it up.

### 2. Obtain an Alpha Vantage API key:
Sign up on [Alpha Vantage](https://www.alphavantage.co/support/#api-key) to get your API key.

### 3. Set up Snowflake:
- Create a Snowflake account if you don’t have one.
- Set up a database and table to store the stock market data.
- You’ll need your Snowflake account details (account URL, username, password, warehouse, database, and schema) to connect to Snowflake.

### 4. Update configuration:
- Open `producer.py` and replace the `API_KEY` variable with your Alpha Vantage API key.
- Open `consumer.py` and replace the Snowflake connection details (account URL, username, password, warehouse, database, and schema).

## Usage

### 1. Kafka Consumer
The consumer listens for stock market data on the Kafka topic `stock_market_data`, writes the data to a file (`stock_market_data_output.json`), and loads it into Snowflake for analysis.

To start the consumer, run:

```bash
python consumer.py
```

### 2. Kafka Producer
The producer fetches real-time stock data from the Alpha Vantage API for the given stock symbol (`TSLA` in this case) and sends it to the Kafka topic `stock_market_data`.

To start the producer, run:

```bash
python producer.py
```

### 3. Snowflake Data Load
Once the consumer consumes the stock market data from Kafka, it loads the data into a Snowflake table. Make sure that the Snowflake database and table schema are created before running the consumer.

### 4. Power BI Visualization
After the stock market data is loaded into Snowflake, use Power BI to create visualizations based on the data. Here’s how to connect Power BI to Snowflake:

1. Open Power BI Desktop.
2. Go to **Get Data** and select **Snowflake**.
3. Enter your Snowflake connection details (account URL, warehouse, database, schema, and login credentials).
4. Load the data and create visualizations (e.g., stock price trends, volume over time).

## Output

**Consumer:** Each stock market data message is written to `stock_market_data_output.json` and loaded into Snowflake with the following schema:

```json
{
  "symbol": "TSLA",
  "timestamp": "2025-01-05 14:30:00",
  "data": {
    "1. open": "702.97",
    "2. high": "710.00",
    "3. low": "700.50",
    "4. close": "705.60",
    "5. volume": "1053500"
  }
}
```

**Producer:** Every minute, the producer fetches the latest stock data and sends it to Kafka.

**Snowflake:** The stock market data is loaded into Snowflake for further analysis and reporting.

**Power BI:** Create dashboards and reports based on the stock market data loaded into Snowflake.

## Troubleshooting

- **Kafka connection issues:** Ensure Kafka is running locally or on a cloud instance and that the broker address is correctly configured in the producer and consumer.
- **API key issues:** If you encounter issues fetching stock data, ensure that your Alpha Vantage API key is valid and correctly configured in `producer.py`.
- **Snowflake connection issues:** Ensure that your Snowflake credentials are correct and that you can connect to the database.
- **Power BI connection issues:** Verify that the Snowflake account URL, warehouse, database, and schema are correctly entered in Power BI.

