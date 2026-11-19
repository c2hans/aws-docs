---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/reference-architectures.html
---

# Reference architectures

This section is a guide to the most common architectures for getting data into an Iceberg lakehouse on AWS, with prescriptive guidance on when to use each one. Every architecture writes to either **Amazon S3 Tables** (fully managed Iceberg) or **self-managed Iceberg on Amazon S3**, and every architecture is compatible with any Iceberg-aware query engine on AWS (Athena, EMR, Glue, Redshift) as well as third-party engines that speak the Iceberg REST catalog API.

## Batch ingestion
<a name="batch-ingestion"></a>

Batch ingestion is the most familiar of these architectures. You'll reach for it when your data arrives on a schedule or in bulk and you don't need second-by-second freshness — the simpler and more cost-effective choice.

![Reference architecture for batch ingestion into Iceberg on AWS, with three stages. On the left, Batch Sources include Amazon S3 data and third-party systems. In the middle, Batch Processor options include AWS Glue ETL, Amazon EMR running Spark batch applications, Amazon EKS and ECS tasks, and AWS Lambda. On the right, the resulting Iceberg tables are stored in either Amazon S3 Tables or self-managed Iceberg tables on Amazon S3.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/ba895846-08e0-4cd3-a7a6-6ace83d96c7e.png)

On the **left**, batch sources include data already sitting in Amazon S3 (CSV, JSON, Parquet, ORC), and data coming from third-party sources — vendor drops, partner feeds, exports from external systems.

In the **middle**, you choose your batch processor:
+ **Amazon EMR** runs Spark batch applications, with both cluster and serverless options. See [Working with Iceberg in Amazon EMR (Spark)](working-with-iceberg-in-amazon-emr-spark.md).
+ **AWS Glue ETL** is also Spark-based and serverless, with built-in connectors and Visual ETL for building pipelines with little or no code. See [Working with Iceberg in AWS Glue](iceberg-glue.md).
+ **Self-managed on Amazon EKS or Amazon ECS** covers container-based workloads — [PyIceberg](iceberg-pyiceberg.md) and **DuckDB** are two lightweight options here.
+ **AWS Lambda** handles event-driven, lightweight batch operations — again, PyIceberg and DuckDB are good fits.

Among these, **EMR and Glue ETL** are the ones you'd reach for when you need heavier transformation, enrichment, or joins over large datasets. **Self-managed ECS/EKS and Lambda** fit lighter loads and event-triggered processing (for example, "a file lands in Amazon S3, convert and append to an Iceberg table").

On the **right**, the processed data lands in your Iceberg tables — self-managed on Amazon S3 or on Amazon S3 Tables.

## Streaming ingestion with a processing framework
<a name="streaming-ingestion-with-a-framework"></a>

Moving from batch to streaming, you'll reach for this pattern when your data arrives as a continuous flow of events that needs to be queryable within seconds/minutes rather than hours — **and** you need to transform, enrich, join, or apply complex event logic to the data in flight. The pattern is three tiers — **stream storage → stream processor → Iceberg**.

![Streaming ingestion reference architecture for Iceberg on AWS. Streaming Storage (Amazon Kinesis Data Streams, Amazon MSK) feeds a Streaming Processor stage with options like Amazon Managed Service for Apache Flink, Amazon EMR with Spark Structured Streaming, AWS Glue Streaming, Amazon MSK Connect with the Iceberg Kafka Sink Connector, Amazon EKS/ECS tasks, and AWS Lambda. Output writes to Iceberg tables in Amazon S3 Tables or self-managed Iceberg on Amazon S3.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/0c8cac5b-8082-4648-8871-52ad4cb324ec.png)

On the **left**, streaming sources — **Amazon Kinesis Data Streams** or **Amazon MSK** — provide the real-time event flow and act as a durable buffer between producers and processors.

In the **middle**, choose your streaming processor:
+ **Amazon Managed Service for Apache Flink** — event-at-a-time processing model with rich support for complex event processing, event-time windowing, streaming joins, and stateful processing. Commits to Iceberg happen at Flink checkpoint boundaries with exactly-once semantics; the connector supports append, overwrite, and upsert writes.
+ **Amazon EMR with Spark Structured Streaming** — Spark-native micro-batch streaming, on a cluster or serverless. Supports the same streaming patterns as Flink (windowed aggregations, streaming joins, stateful processing, complex event logic), within a micro-batch model. Pick this when your team already uses Spark and wants a unified batch \+ streaming codebase. See [Working with Iceberg in Amazon EMR (Spark)](working-with-iceberg-in-amazon-emr-spark.md).
+ **AWS Glue Streaming** — additional serverless variant of the Spark micro-batch model, with built-in connectors and Visual ETL for building the pipeline with little or no code. Same streaming capabilities as EMR Spark Structured Streaming. See [Working with Iceberg in AWS Glue](iceberg-glue.md).
+ **Amazon MSK Connect with the Iceberg Kafka Sink Connector** — a no-code, connector-based approach that streams straight from Kafka into Iceberg with multi-table fan-out.
+ **Self-managed on Amazon EKS or Amazon ECS** — container-based custom processors, with [PyIceberg](iceberg-pyiceberg.md) and **DuckDB** as two lightweight options.
+ **AWS Lambda** — event-driven, lightweight micro-batch pattern, PyIceberg and DuckDB as two lightweight options.

Each option carries different trade-offs in latency, throughput, and operational complexity:
+ **Flink, EMR Spark Structured Streaming, and Glue Streaming** are the ones you'd reach for when you need real streaming processing — windowed aggregations, streaming joins, enrichment, stateful processing, or complex event processing.
+ **MSK Connect** fits straightforward, no-code streaming from Kafka into Iceberg with no processing in between.
+ **Self-managed ECS/EKS or Lambda** fit custom implementations where you want full control, typically for lighter workloads with minimal transformation.

On the **right**, the processed data lands in your Iceberg tables — self-managed on Amazon S3 or on Amazon S3 Tables. Because streaming produces many small files, plan for regular compaction — see [Maintaining Iceberg tables](maintaining-iceberg-tables.md).

## Low-code streaming with Amazon Data Firehose
<a name="low-code-streaming-with-amazon-data-firehose"></a>

Amazon Data Firehose is the lightweight counterpart to the pattern above — where the previous section was about rich processing of data in flight, here you reach for Firehose when you want streaming or log data landed in Iceberg with minimal effort and no processing job to write or manage. In the simplest case, no code is needed at all — though simple per-record transforms are possible if you need them. What Firehose **won't** do is the stateful, complex event processing that Flink or Spark give you.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/5bae2457-fb7a-412d-961e-e324af514ee2.png)

Data gets into Firehose through three paths:
+ **Direct puts** using the AWS SDK.
+ **Natively supported sources** — WAF logs, VPC Flow Logs, CloudWatch Logs and Metrics, Fluentd, Fluentbit, EventBridge, Lambda, SNS, Route 53 resolver query logs, and more.
+ **Attaching Firehose directly to Amazon Kinesis Data Streams or Amazon MSK** as a delivery stream consumer.

From there, Firehose writes directly to your Iceberg tables — self-managed on Amazon S3 or on Amazon S3 Tables — with no processing job to manage. You control how the data is batched before it's written, by buffer size or by time interval. If you do want simple, per-record transforms — reformatting, filtering, or enriching individual records before writing — you can add an optional Lambda function.

Firehose also gives you **fan-out from one delivery stream to many Iceberg tables** (route records to different tables based on content, without splitting the stream upstream). Where duplicates matter, define unique keys on the table and use the `update` operation, which makes redelivery of the same record idempotent; the default `insert` operation preserves duplicates. For details, see [Working with Iceberg tables by using Amazon Data Firehose](iceberg-firehose.md).

## Change data capture (CDC)
<a name="change-data-capture-cdc"></a>

Change data capture is a variation of streaming. You'll reach for it when the data you want isn't a flow of new events but the ongoing changes happening inside an operational database.

![CDC reference architecture for Iceberg on AWS. A source RDBMS (Amazon RDS) is captured by Amazon MSK Connect with the Debezium connector, which sends CDC records to Amazon MSK. A Streaming Processor consumes from MSK via Amazon Managed Service for Apache Flink, Amazon EMR with Spark Structured Streaming, AWS Glue Streaming, Amazon MSK Connect with the Iceberg Kafka Sink Connector, EKS/ECS tasks, or AWS Lambda, writing to Iceberg tables in Amazon S3 Tables or self-managed Iceberg on S3.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/dba6d8e8-ddee-4524-ab61-e6af50ea7193.png)

The architecture adds two things to the streaming pattern:

1. **A source database** on the left — typically Amazon RDS, Amazon Aurora, or any relational database that exposes a transaction log (WAL / binlog / redo log). This applies to on-premises PostgreSQL, MySQL, SQL Server, and Oracle as well.

1. **A CDC capture mechanism** that detects those changes. The diagram shows **Amazon MSK Connect with the Debezium connector**, which reads row-level changes from the source database's transaction log and publishes them to Kafka topics on Amazon MSK. The same pattern works with any log-based CDC tool that can publish to Kafka — for example **Oracle GoldenGate for Big Data**. Log-based capture is non-invasive — no triggers, no performance impact on the source.

From there, the CDC events flow through the **same streaming processors** covered in the previous [Streaming ingestion with a processing framework](#streaming-ingestion-with-a-framework)** **section, with the same trade-offs, and land in Iceberg tables — self-managed on Amazon S3 or on Amazon S3 Tables.

For CDC specifically, one more distinction matters between the processing engines — **how each one applies the changes to the Iceberg table**:
+ **Amazon EMR / AWS Glue with Spark** can run the full Iceberg `MERGE INTO` operation — inserts, updates, and deletes — reconciling changes into a current-state table in one shot.
+ **Amazon Managed Service for Apache Flink and PyIceberg** support upsert and delete. Combining the two gives you full materialization of the current state.
+ **Amazon MSK Connect with the Iceberg Kafka Sink Connector** is append-only. It's a good fit for landing the raw CDC stream — each change written as a row, typically consolidated later by a separate ETL job — but not for directly materializing the current state.

Two design decisions to think through:
+ **Append-only vs. materialized current state.** Landing raw change events (`I`, `U`, `D` with timestamps) in an append-only Iceberg table gives you complete history at the cost of storage and downstream deduplication logic. Applying the changes with `MERGE INTO` (or upsert \+ delete) gives you a compact current-state table at the cost of losing raw history. Many customers land the raw events first, then materialize a current-state view on top with a scheduled job or a materialized view.
+ **Update strategy.** For high-frequency updates, merge-on-read reduces write amplification but shifts cost to readers (and to any writer that has to re-read the table for the next `MERGE`). See [Choose the right update strategy](optimizing-read-and-write-performance.md).

## Zero-ETL
<a name="zero-etl"></a>

Zero-ETL is the pattern to consider when you want your source data mirrored **as-is** into Iceberg format — so you can run complex analytics on it that would be hard to do performantly or cost-effectively against the source system.

![Zero-ETL reference architecture for Iceberg on AWS. Sources include AWS databases such as Amazon DynamoDB and third-party applications such as Salesforce, SAP, ServiceNow, Zendesk, Zoho CRM, Facebook Ads, Salesforce Marketing, and Instagram Ads. AWS Glue Zero-ETL ingests data directly from these sources into Iceberg tables stored in Amazon S3 Tables or self-managed Iceberg on Amazon S3, without a separate extract, transform, and load pipeline.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/57b9e793-7915-44af-9716-b35d5fdce243.png)

Zero-ETL removes the ETL pipeline: data moves from source to Iceberg **without any transformation code in between**. On AWS this is delivered through **AWS Glue Zero-ETL**, which lands the data directly into Iceberg tables — self-managed on Amazon S3 or on Amazon S3 Tables — from sources such as:
+ **SaaS applications** — Salesforce, SAP, ServiceNow, Zendesk, Zoho CRM, Facebook Ads, Salesforce Marketing, Instagram Ads, and more.
+ **AWS databases** — Amazon DynamoDB.

It works as an **initial load** followed by **incremental propagation** — changes at the source flow into the Iceberg copy automatically, so it stays current without you managing any processing infrastructure. From there, the data is ready to query with Amazon Athena, Amazon Redshift, or any other Iceberg-compatible engine.

The trade-off is **less control over transformations**, so Zero-ETL fits best when your source data is already close to your desired analytical shape. When you need reshaping, joins, or enrichment before Iceberg, use one of the batch or streaming patterns above instead.

## Streaming tables - direct managed ingestion
<a name="streaming-tables-direct-managed-ingestion"></a>

Use streaming tables when you want to land a single Kafka topic or Kinesis stream as a queryable Iceberg table with **zero infrastructure between the stream and the table** — no connectors to size, no Flink or Spark job to write, no custom consumer to run. This is the simplest streaming ingestion path and often the cheapest for pure append-only workloads.

![Streaming tables reference architecture for Iceberg on AWS. Streaming events land in a Streaming Storage stage made up of Amazon Kinesis Data Streams and Amazon MSK Express, and are ingested directly into Iceberg tables in Amazon S3 Tables through the managed streaming tables feature, without a separate streaming processor.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/c5769dbd-f5b2-4af1-9e87-77370cfe52c5.png)

The service continuously materializes topic (or stream) data as read-only Iceberg tables on Amazon S3 Tables, applies inline compaction so downstream queries hit properly sized Parquet files, and auto-registers the table in the AWS Glue Data Catalog so any Iceberg-aware engine (Athena, Redshift, EMR, Flink, and third-party engines) can query it immediately.

Two source-side flavors, both writing to Iceberg on Amazon S3 Tables:
+ **Streaming tables from Amazon MSK Express Brokers** — for Kafka-native producers.
+ **Streaming tables from Amazon Kinesis Data Streams On-demand / On-demand Advantage** — for producers already using KDS.

Both flavors share the same characteristics:
+ **Schema:** a schema registered in AWS Glue Schema Registry is required. Records are plain JSON validated against a schema ARN you provide, or GSR-serialized JSON with the schema ID embedded in each record. Schema evolution is not supported: to change the schema, create a new streaming table.
+ **Partitioning:** hourly, by event time.
+ **Data freshness:** 5 to 15 minutes; the default is 10.
+ **Output:** read-only Iceberg tables on Amazon S3 Tables, written as Parquet with inline compaction; S3 Tables runs the remaining maintenance.
+ **Ingestion mode:** append-only (new rows only; for CDC-style upserts, use [Change data capture](#change-data-capture-cdc) instead).
+ **Source requirements:** Amazon MSK Provisioned clusters with Express brokers (Standard brokers and MSK Serverless are not supported); Amazon Kinesis Data Streams in On Demand Standard or On Demand Advantage capacity mode, with a dead-letter queue for records that fail schema validation.

For more information, see [Streaming directly to Iceberg from Amazon Kinesis Data Streams and Amazon MSK](streaming-directly-to-iceberg-from-kinesis-and-msk.md).

## Interoperability and AWS Glue Iceberg catalog federation
<a name="interoperability-and-aws-glue-iceberg-catalog-federation"></a>

There may be cases where Iceberg tables are spread across multiple catalogs — your AWS lakehouse in the AWS Glue Data Catalog on one side, and tables managed elsewhere (Snowflake Horizon, Databricks Unity Catalog managed or open source, Apache Polaris, or any custom Iceberg REST catalog) on the other. With **AWS Glue Iceberg catalog federation**, you register those remote catalogs into the AWS Glue Data Catalog. Any client that speaks the Iceberg REST Catalog API can then reach the federated tables through the **AWS Glue Iceberg REST catalog endpoint** — you get a **unified view** across catalogs with **central governance** through the AWS Glue Data Catalog and AWS Lake Formation, and **no data copies**.

![AWS Glue Iceberg catalog federation. Remote catalogs (Databricks Unity Catalog, Snowflake Horizon/Polaris, open source Iceberg REST catalog) point to Iceberg tables in Amazon S3. AWS Glue Data Catalog holds federated entries (unity_federated_catalog, snowflake_federated_catalog, oss_iceberg_rest_federated_catalog) plus a local_catalog, with AWS Lake Formation governance. Consumers (Athena, Redshift, EMR, Spark, any Iceberg client) query Glue and read data directly from S3.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/28137c2c-d83c-4dfb-b2a1-ddd5be19195a.png)

How it works:
+ The **AWS Glue Data Catalog acts as a unified metadata layer** over your own tables and the federated remote catalogs.
+ At query runtime, Glue reaches out to the remote REST catalog to resolve metadata, then the engine reads the data files directly from the remote storage location.
+ **AWS Lake Formation** applies fine-grained permissions on top — table, column, and row-level filters — so you keep governance over who can access what across catalogs.

Federation is currently **read-only**, which covers the most common cross-catalog use cases: joining tables across platforms, building unified dashboards, and accessing live data without moving it or using the source platform's compute.

For detailed setup and the full list of supported remote catalogs, see [Catalog federation for Apache Iceberg tables in the AWS Glue Data Catalog](catalog-federation-for-apache-iceberg-tables.md).
