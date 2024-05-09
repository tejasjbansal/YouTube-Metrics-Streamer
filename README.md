# YouTube Metrics Streamer

## Overview
The YouTube Metrics Streamer is a Python-based application designed to fetch real-time metrics such as likes, views, comments, and favorites from YouTube videos, and stream this data through Apache Kafka. It utilizes Confluent Kafka and KsqlDB for stream processing, with the processed data being dispatched to a Telegram bot for real-time notifications. This project is ideal for developers interested in real-time data processing and integration of various technologies like Kafka, KsqlDB, and Telegram.


## Project Architecture
![Blank diagram](https://github.com/tejasjbansal/YouTube-Metrics-Streamer/assets/56173595/a3d3cf35-29da-4b80-be34-af133e4f6503)


## Project Components
- **Data Source**: Fetches data from the YouTube API.
- **Python**: Responsible for retrieving data from the YouTube API and publishing it to Kafka.
- **Confluent Kafka and Schema Registry**: Manages the streaming data infrastructure in the cloud.
- **KsqlDB and Connect**: Processes streaming data from Kafka topics using KsqlDB for real-time analytics.
- **Telegram**: Delivers the analytics results to end users through real-time notifications on a Telegram bot.

## Technologies Used
- Python 3.10 (minimum required)
- Apache Kafka
- Telegram API
- Docker
- Confluent Platform (includes Zookeeper, Kafka, Schema Registry, Connect, ksqlDB, and Control Center)

## Getting Started

### Prerequisites
Before you begin, ensure you have Docker installed on your machine. This project uses Docker to run Confluent Kafka, Schema Registry, and other components effortlessly.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tejasjbansal/youtube-metrics-streamer.git
   cd youtube-metrics-streamer
   ```

2. **Setup Confluent Kafka environment using Docker**
   ```bash
   docker-compose up -d
   ```

   This command will start all the necessary services defined in the `docker-compose.yml` file, including Zookeeper, Kafka, Schema Registry, Connect, ksqlDB, and Control Center.

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **API Key and Token**
   - Insert your API's in the appropriate configuration file or environment variable such as `YOUTUBE_API_KEY`, `KAFKA_BOOTSTRAP_SERVERS`, and `TELEGRAM_BOT_TOKEN`.

### Running the Application
To start the application, execute the following commands:

```bash
python YoutubeAnalytics.py
```

## Usage
Once the application is running, it will:
- Fetch YouTube video metrics at regular intervals.
- Stream the data to Kafka.
- Process the data using KsqlDB.
- Send real-time analytics results to a Telegram bot.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests as appropriate.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.


