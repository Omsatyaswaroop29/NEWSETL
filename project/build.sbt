name := "KafkaSparkStreaming"
version := "0.1"
scalaVersion := "2.12.10"

// Adding resolvers for Maven Central to ensure all dependencies can be found
resolvers += "Apache Maven Central" at "https://repo1.maven.org/maven2"

// Defining all Spark and related dependencies, excluding conflicting logging libraries
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.1.2",
  "org.apache.spark" %% "spark-sql" % "3.1.2",
  "org.apache.spark" %% "spark-streaming" % "3.1.2",
  "org.apache.spark" %% "spark-sql-kafka-0-10" % "3.1.2",
  "org.elasticsearch" %% "elasticsearch-spark-30" % "7.17.1",
  "ch.qos.logback" % "logback-classic" % "1.2.3"
)

.map(_.excludeAll(
  ExclusionRule(organization = "org.slf4j", name = "slf4j-log4j12"),
  ExclusionRule(organization = "log4j")
))

// Configuration for running the application
fork := true
javaOptions ++= Seq(
  "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED",
  "--add-opens=java.base/java.io=ALL-UNNAMED",
  "--add-opens=java.base/java.lang=ALL-UNNAMED",
  "--add-opens=java.base/java.util=ALL-UNNAMED",
  "--add-opens=java.base/java.nio=ALL-UNNAMED",
  "-Dorg.slf4j.simpleLogger.defaultLogLevel=debug"
)
