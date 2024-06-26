import streamlit as st
from elasticsearch import Elasticsearch
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Elasticsearch configuration
es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

def fetch_data_from_elasticsearch(index_name):
    try:
        response = es.search(index=index_name, body={"query": {"match_all": {}}}, size=1000)
        return response['hits']['hits']
    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
        return []

def transform_data_to_dataframe(hits):
    data = []
    for hit in hits:
        source = hit["_source"]
        data.append({
            "Title": source.get("Title", "No Title Available"),
            "URL": source.get("URL", "#"),
            "Source": source.get("Source", "Unknown"),
            "Published Date": source.get("Published Date", "Unknown Date"),
            "Description": source.get("Description", "No description available."),
        })
    return pd.DataFrame(data)

def main():
    st.title("Real-Time News Dashboard")

    index_name = st.text_input("Enter the Elasticsearch index name:", "news_index")

    if st.button("Fetch Data"):
        hits = fetch_data_from_elasticsearch(index_name)
        if hits:
            df = transform_data_to_dataframe(hits)
            st.write(df)
        else:
            st.write("No data found in the index.")

if __name__ == "__main__":
    main()
