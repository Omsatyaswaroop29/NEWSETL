import os
import requests
from dotenv import load_dotenv
from kafka import KafkaProducer
import json

# Load environment variables
load_dotenv()

# API Endpoints and Keys
API_KEYS = {
    "serp": os.getenv('SERP_API_KEY'),
    "newsapi": os.getenv('NEWS_API_KEY'),
}

# Debugging: Print the loaded API keys to verify
print(f"SERP_API_KEY: {API_KEYS['serp']}")
print(f"NEWS_API_KEY: {API_KEYS['newsapi']}")

if not API_KEYS['newsapi']:
    raise ValueError("NewsAPI key not found. Ensure it's set in the .env file.")
if not API_KEYS['serp']:
    raise ValueError("SERP API key not found. Ensure it's set in the .env file.")

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def fetch_news_from_newsapi(query):
    """Fetches news using NewsAPI."""
    url = "https://newsapi.org/v2/everything"
    params = {
        'apiKey': API_KEYS['newsapi'],
        'q': query,
        'language': 'en',
        'pageSize': 10,  # Adjust pageSize as needed
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        print(f"Error fetching from NewsAPI: {response.status_code}, {response.text}")
        return []

def transform_articles(articles):
    """Transforms raw articles to a structured format with clear labeling."""
    transformed = []
    for article in articles:
        transformed.append({
            "Title": article.get("title", "No Title Available"),
            "URL": article.get("url", "#"),
            "Source": article['source']['name'] if 'source' in article else "Unknown",
            "Published Date": article.get("publishedAt", "Unknown Date"),
            "Description": article.get("description", "No description available."),
        })
    return transformed

def load_data_to_kafka(data):
    """Sends data to a Kafka topic."""
    for item in data:
        producer.send('news_topic', value=item)
        producer.flush()
    print("Data sent to Kafka successfully.")

def main():
    query = "global warming"  # Modify query to fit your interest
    try:
        newsapi_articles = fetch_news_from_newsapi(query)
        if newsapi_articles:
            transformed_data = transform_articles(newsapi_articles)
            load_data_to_kafka(transformed_data)
        else:
            print("No articles fetched.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
