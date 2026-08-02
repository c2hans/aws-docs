---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-modern-data-streaming-analytics-architectures/key-considerations-while-building-streaming-analytics.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Key considerations while building streaming analytics
<a name="key-considerations-while-building-streaming-analytics"></a>

 When you are building a streaming data pipeline using modern data architecture to stream log and event data to power live dashboards and deliver data into data lakes, to build real-time analytics and event-driven applications and machine learning (ML), you must first understand the ideal usage patterns of AWS streaming data solutions, your user personas, and your specific use case so you can choose the right service for the job.

## Choosing the right Kinesis service for your use case
<a name="choosing-the-right-kinesis-service-for-your-use-case"></a>

 The following table illustrates the ideal usage patterns of various Kinesis data streaming and processing services.

* Table 1: Amazon Kinesis usage patterns *

|   |  Kinesis Data Streams  |  Firehose  |  Managed Service for Apache Flink  |
| --- | --- | --- | --- |
|  Usage  | Capture stream log and event data, run real-time analytics, and build event-driven applications | Load data streams into AWS data stores | Analyze data streams with Managed Service for Apache Flink Studio and Apache Flink |
|  Data sources  | Mobile apps, application logs, web clickstream/social, IoT sensors, connected products, smart buildings  | Connected devices such as consumer appliances, embedded sensors, TV set-top boxes, clickstream data, application logs  | Analyze streaming data from Kinesis Data Streams, Amazon MSK, [Amazon MQ](https://aws.amazon.com/amazon-mq/), custom connectors  |
|  Stream ingestion  | [AWS SDKs](https://aws.amazon.com/tools/), [Kinesis Producer Library](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-kpl.html), [AWS Mobile SDKs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-mobile-sdks.html), [Kinesis Agent](https://docs.aws.amazon.com/streams/latest/dev/writing-with-agents.html), [AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/kinesis-rule-action.html), [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RelayEventsKinesisStream.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html) | AWS SDKs, Kinesis Producer Library, Kinesis Data Streams, Kinesis Agent, AWS IoT, Amazon CloudWatch Events  | Analyze streaming data from Kinesis Data Streams, Amazon MSK, Amazon MQ, custom connectors  |

## Choosing the right streaming service for your use case
<a name="choosing-the-right-streaming-for-your-use-case"></a>

 The following table Illustrates the comparison between Apache Kafka, Kinesis Data Streams, and Amazon MSK**.**

 *Table 2 — Streaming services *

|  Attribute  |  Apache Kafka  |  Kinesis Streams  |  MSK  |
| --- | --- | --- | --- |
|  Ease of use  |  Advanced setup required  |  Get started in minutes  |  Get started in minutes  |
|  Management Overhead  |  High  |  Low  |  Low (Amazon MSK Serverless) to Medium (Amazon MSK Provisioned)  |
|  Scalability  |  Difficult to scale  |  Scale in seconds with one click  |  Scale in minutes with one click  |
|  Throughput  |  Very large  | Scale with Kinesis Data Streams on-demand |  Very large  |
|  Infrastructure  |  You manage  |  AWS manages  |  AWS manages  |
|  Open-sourced?  |  Yes  |  No  |  Yes (managed service for Apache Kafka)  |
| Data rentention | You can retain data for longer duration, and it is configurable. | You can retain data for up to 365 days. | You can retain data for longer duration, and it is configurable. With the tiered storage feature of Amazon MSK, you can cost-efficiently store vast amounts of data in Amazon S3. |
| Latency | Low | Low (70ms with Enhance Fan Out) | Lowest |

## Choosing the right streaming data processing technology
<a name="streaming-data-processing-technologies"></a>

 Streaming data processing technologies support many use cases that include event-driven applications, data analytics applications, and data pipeline applications. Commonly used frameworks include [Apache Kafka Streams](https://kafka.apache.org/documentation/streams/), [Apache Flink](https://flink.apache.org/), [KSQL](https://www.confluent.io/online-talks/intro-to-ksql-streaming-sql-for-apache-kafka/), and Managed Service for Apache Flink for Flink. Apache Kafka Streams, [Apache Flink](https://flink.apache.org/), and KSQL are open-source options, while Amazon Managed Service for Apache Flink offers a fully managed Apache Flink.

 The following table Illustrates the comparison between Apache Kafka Streams, Managed Service for Apache Flink for Apache Flink, and Managed Service for Apache Flink SQL.

 *Table 3 — Comparison between data stream processing technologies*

|  Feature  |  Apache Kafka Streams  |  Managed Service for Apache Flink for Apache Flink  |  Kinesis Client Library  |  Lambda  |
| --- | --- | --- | --- | --- |
|  Open source  |  Yes  |  Based on open-source Apache Flink  |  Based on Kinesis [Client Library for Java](https://github.com/awslabs/amazon-kinesis-client) open source  |  No, based on proprietary engine  |
|  Sources  |  Kafka only  |  Kinesis Data Streams, Amazon MSK for Apache Kafka, DynamoDB, custom sources, [RabbitMQ](https://aws.amazon.com/about-aws/whats-new/2020/11/announcing-amazon-mq-rabbitmq/) [RabbitMQ](https://aws.amazon.com/about-aws/whats-new/2020/11/announcing-amazon-mq-rabbitmq/)  |  Kinesis Data Streams  |  Kinesis Data Streams, Firehose, Amazon MSK  |
|  Destination/sinks  |  Kafka only; over 10 connectors supported with Kafka connect  |  Amazon MSK for Kafka, Kinesis Data Streams, Firehose, Amazon S3 Apache Cassandra, Amazon DynamoDB, OpenSearch Service, custom sinks supported by open-source Flink  |  Multi-stream processing  |  Use AWS Lambda to respond to or adjust immediate occurences within the event-driven applications. AWS Lambdacan read records from Kinesis Data Streams and invokes your function.  |
|  Development languages  |  Java and Scala  |  Java, Scala, SQL, and Python  |  Java; support for languages other than Java is provided using a multi-language interface called the MultiLangDaemon  |  Java, .NET Core, Go, PowerShell, Node.js\#, Python, Ruby; it supports multiple languages through the use of [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)  |
|  Development process  |  Develop on any integrated development environment (IDE) using Java or Scala. The application is separate from the Kafka broker and needs to be scaled independently.  |  Develop on any IDE and build a JAR ﬁle. Create a Managed Service for Apache Flink Flink application and upload application JAR.  |  The Kinesis Client Library (KCL) is a Java library. KCL helps you consume and process data from a Kinesis data stream by taking care of many of the complex tasks, such as load balancing across multiple consumer application instances, responding to consumer application instance failures, checkpointing processed records, and reacting to resharding.  |  Develop on any IDE that is supported by respective programming language  |
|  Exactly once processing support  |  Yes  |  Yes  |  Not built in  |  Not built in  |
|  Per record processing latency  |  Sub-second  |  Sub-second  |  Seconds  |  Seconds  |
|  Batch support  |  No  |  Yes, supported by Flink  |  No  |  Yes, with Amazon EventBridge  |
