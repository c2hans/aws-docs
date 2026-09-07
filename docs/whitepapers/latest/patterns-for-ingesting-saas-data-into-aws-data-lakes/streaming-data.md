---
source_url: https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/streaming-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Streaming data
<a name="streaming-data"></a>

## Amazon Managed Streaming for Apache Kafka and Amazon Kinesis: Introduction
<a name="amazon-managed-streaming-for-apache-kafka-and-amazon-kinesis"></a>

 [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK) makes it easy to ingest and process streaming data in real time with fully-managed Apache Kafka.

 [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) is an ETL service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services.

### Architecture overview
<a name="architecture-overview-3"></a>

 Often, use cases require the source data to be to immediately made available in the data lake for analytics. Getting the data from the SaaS application in near-real-time lays the foundation for an event-driven architecture. Start with how Apache Kafka helps with this architecture pattern: Apache Kafka has a tool called [Kafka Connect](https://kafka.apache.org/documentation/#connect), which allows for scalable and reliable streaming data between Apache Kafka and other systems. Many SaaS applications allow for events data to be published to Kafka topics using Kafka Connect.

 Amazon MSK eliminates the operational overhead, including the provisioning, configuration, and maintenance of highly-available Apache Kafka and Kafka Connect clusters. With [Amazon MSK Connect](https://aws.amazon.com/msk/features/msk-connect/), a feature of Amazon MSK, you can run fully-managed Apache Kafka Connect workloads on AWS. This feature makes it easy to deploy, monitor, and automatically scale connectors that move data between Apache Kafka clusters and external systems. Amazon MSK Connect is fully-compatible with Kafka Connect, enabling you to lift and shift your Kafka Connect applications with zero code changes. With Amazon MSK Connect, you only pay for connectors you are running, without the need for cluster infrastructure.

 Once the data is streamed in Kafka, you can either directly send it to Amazon S3 or you can use the [Kinesis-Kafka Connector](https://github.com/awslabs/kinesis-kafka-connector) to extend the pipeline before the data is pushed into Amazon S3. The advantage of using Firehose in the streaming data pipeline is that you can now transform/normalize the events data, buffer it for a specific interval or a specific file size, and finally convert this data into Parquet file format before it lands in Amazon S3. You can also partition the data in Amazon S3 prefixes based on rules using Firehose.

![This is a diagram that displays a data-based ingestion pattern between SaaS applications, Amazon Managed Kafka, Amazon Kinesis Firehose, and Amazon S3.](https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/images/streaming-based-data-ingestion-pattern.png)

### Usage patterns
<a name="usage-patterns-3"></a>

 This pattern is handy when you want to stream data changes from SaaS applications into your Amazon S3 data lake in near-real-time.

 Some use cases are as follows:
+  Real-time analytics dashboards.
+  External, API-driven applications.

### Considerations
<a name="considerations-3"></a>

 The above architecture pattern adds all records in Amazon S3 as new data. To handle updates and deletes in the data lake, you may have to use AWS Glue, streaming with [Apache Hudi connector](https://aws.amazon.com/blogs/big-data/writing-to-apache-hudi-tables-using-aws-glue-connector/), to correctly identify and update the existing records in Amazon S3.
