package com.example

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object KafkaSparkStreaming {
  
  def main(args: Array[String]): Unit = {
    // Initialize SparkSession with Elasticsearch configurations
    val spark = SparkSession.builder()
      .appName("KafkaSparkStreaming")
      .config("spark.es.index.auto.create", "true")
      .config("spark.es.nodes", "172.18.0.2") // Set to your Elasticsearch host IP
      .config("spark.es.port", "9200")       // Set to your Elasticsearch port
      .getOrCreate()

    // Set the log level to minimize verbose output
    spark.sparkContext.setLogLevel("WARN")

    // For implicit conversions like converting RDDs to DataFrames
    import spark.implicits._

    // Check if 'streaming' is a part of command-line arguments to start streaming job
    if (args.contains("streaming")) {
      val kafkaParams = Map(
        "kafka.bootstrap.servers" -> "localhost:9092",  // Kafka broker address
        "subscribe" -> "news_topic",                    // Kafka topic to subscribe to
        "startingOffsets" -> "earliest"                 // Start reading from the earliest message
      )

      // Read data from Kafka
      val kafkaDF = spark.readStream
        .format("kafka")
        .options(kafkaParams)
        .load()

      // Transform the data; casting 'value' to string and adding a timestamp
      val newsDF = kafkaDF
        .selectExpr("CAST(value AS STRING) as value")
        .withColumn("timestamp", current_timestamp())

      // Write the stream to Elasticsearch
      val query = newsDF.writeStream
        .outputMode("append")
        .format("es")
        .option("checkpointLocation", "/tmp/spark-checkpoints") // Checkpoint location for fault tolerance
        .start("news_index/news_type")  // Elasticsearch index and type

      // Await termination to keep the stream running
      query.awaitTermination()
    } else {
      println("Please specify 'streaming' to start the streaming job.")
    }
  }
}
