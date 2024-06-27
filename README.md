
# News Collector and Real-Time Dashboard

## Overview

This project constructs a robust ETL (Extract, Transform, Load) pipeline for collecting, processing, and visualizing news articles in real time. Utilizing the News API, Apache Kafka, Apache Spark, and Elasticsearch, this system ensures efficient data handling and provides dynamic insights through Kibana and custom-built Streamlit dashboards.

## Project Statement

The goal of this project is to develop a scalable and efficient pipeline for real-time news collection and visualization, enabling users to access timely and insightful data analyses through interactive interfaces.

## Project Goals

- **Efficient Data Collection**: Automate the extraction of news articles using the News API.
- **Real-Time Data Processing**: Leverage Apache Kafka for message brokering and Apache Spark for stream processing.
- **Reliable Data Storage**: Employ Elasticsearch for robust data storage and quick retrieval capabilities.
- **Interactive Visualization**: Utilize Kibana for advanced data visualization and Streamlit for custom, user-friendly dashboards.
- **Scalability and Isolation**: Use Docker to containerize and manage the software environment, ensuring consistency across different setups.
- 


<div style="display: flex; flex-direction: column; align-items: flex-start; justify-content: center; padding: 20px;">
    <div style="text-align:center; margin: 20px; margin-left: 0px; width: 200px;">
        <img src="https://databar.ai/media/external_source_logo/NewsAPI_QjWnptB.png" alt="News API" width="100" height="100"><br/>
        <strong>News API</strong>
    </div>
    <div style="text-align:center; margin: 20px; margin-left: 50px; width: 200px;">
        <img src="https://www.ovhcloud.com/sites/default/files/styles/text_media_horizontal/public/2021-09/ECX-1909_Hero_Kafka_600x400%402x-1.png" alt="Kafka" width="100" height="100"><br/>
        <strong>Kafka</strong>
    </div>
    <div style="text-align:center; margin: 20px; margin-left: 100px; width: 200px;">
        <img src="https://www.azul.com/wp-content/uploads/2021/03/technologies-spark.png" alt="Spark" width="100" height="100"><br/>
        <strong>Spark</strong>
    </div>
    <div style="text-align:center; margin: 20px; margin-left: 150px; width: 200px;">
        <img src="https://miro.medium.com/v2/resize:fit:1000/1*Oh6M-X2E6lNuSO9XtfYYkQ.png" alt="Elasticsearch" width="100" height="100"><br/>
        <strong>Elasticsearch</strong>
    </div>
    <div style="text-align:center; margin: 20px; margin-left: 200px; width: 200px;">
        <img src="https://www.saagie.com/wp-content/uploads/elementor/thumbs/Kibana-q3vwhyub1i9wgbo7j1k4tk0web4r6o41n9euhv6rk0.png" alt="Kibana" width="100" height="100"><br/>
        <strong>Kibana</strong>
    </div>
    <div style="text-align:center; margin: 20px; margin-left: 250px; width: 200px;">
        <img src="https://30days-tmp.streamlit.app/~/+/media/c1d64cbe224f2a71943d37c5294f12c656d9379b6b866e3f418fe9aa.png" alt="Streamlit" width="100" height="100"><br/>
        <strong>Streamlit</strong>
    </div>
    <div style="text-align:center; margin: 20px; margin-left: 300px; width: 200px;">
        <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/97_Docker_logo_logos-512.png" alt="Docker" width="100" height="100"><br/>
        <strong>Docker</strong>
    </div>
</div>





## Features

- **Automated News Collection**: Utilizes News API to fetch current news articles.
- **Streamlined Data Processing**: Implements Apache Spark and Kafka to process data in real time.
- **Robust Data Storage**: Stores processed data in Elasticsearch for efficient querying and retrieval.
- **Advanced Visualization Tools**: Employs Kibana for detailed data visualization and Streamlit for creating interactive, custom dashboards.
- **Containerized Deployment**: Integrates Docker for easy and consistent deployment across environments.

## Technologies Used

- **News API**: Fetches real-time news data.
- **Apache Kafka**: Manages real-time data streams.
- **Apache Spark**: Processes data in real time.
- **Elasticsearch**: Indexes and stores data.
- **Kibana**: Visualizes data.
- **Streamlit**: Develops custom interactive dashboards.
- **Docker**: Containerizes applications to ensure environmental consistency.

## ETL Process

1. **Extract**: News articles are dynamically fetched from News API.
2. **Transform**: Data is processed in real-time using Apache Spark to structure and analyze the content.
3. **Load**: The structured data is stored in Elasticsearch, making it readily available for analysis and visualization.

## Setup Instructions

### Prerequisites

- Docker & Docker Compose
- Python 3.x
- Scala Build Tool (sbt)
- Git

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Omsatyaswaroop29/NEWSETL.git
   cd NEWSETL
   ```

2. **Set Up Environment Variables**:
   ```env
   SERP_API_KEY=your_serp_api_key
   NEWS_API_KEY=your_news_api_key
   ```

3. **Start Docker Containers**:
   ```bash
   docker-compose up -d
   ```

4. **Build and Run the Scala Application**:
   ```bash
   sbt clean compile run
   ```

5. **Run the News Extractor**:
   ```bash
   pip install -r requirements.txt
   python news_extractor.py
   ```

6. **Launch the Streamlit Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

## Usage

- **Fetch News**: Automated scripts collect data from News API and send it to Kafka.
- **Process Data**: The Scala application processes this data in real-time using Spark and sends it to Elasticsearch.
- **Visualize Data**: Data is visualized through Kibana and the custom Streamlit dashboard.

## Dashboard

Explore interactive visualizations and real-time news data insights via the custom Streamlit dashboard. Filter, search, and analyze news articles to uncover trends and patterns.

## License

MIT License

Copyright (c) 2024 Omsatyaswaroop29

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
