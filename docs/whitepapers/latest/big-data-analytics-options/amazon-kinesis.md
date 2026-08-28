---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-kinesis.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Kinesis
<a name="amazon-kinesis"></a>

 Amazon Kinesis is a platform for streaming data on AWS that makes it easy to load and analyze streaming data. Amazon Kinesis also enables you to build custom streaming data applications for specialized needs. With Kinesis, you can ingest real-time data such as application logs, website clickstreams, Internet of Things (IoT) telemetry data, and more into your databases, data lakes, and data warehouses, or build your own real-time applications using this data. Amazon Kinesis enables you to process and analyze data as it arrives and respond in real-time instead of having to wait until all your data is collected before the processing can begin.

 Currently there are four pieces of the Kinesis platform that can be utilized based on your use case:
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) enables you to build custom applications that process or analyze streaming data.
+  [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) enables you to build custom applications that process or analyze streaming video.
+  [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) enables you to deliver real-time streaming data to AWS destinations such as [Amazon S3](https://aws.amazon.com/s3/), [Amazon Redshift](https://aws.amazon.com/redshift/), [OpenSearch Service](https://aws.amazon.com/opensearch-service/), and [Splunk](https://aws.amazon.com/quickstart/architecture/splunk-enterprise/).
+  [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/) enables you to process and analyze streaming data with standard SQL or with Java (managed [Apache Flink](https://flink.apache.org/)).

[Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) and [Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) enable you to build custom applications that process or analyze streaming data in real time. Kinesis Data Streams can continuously capture and store terabytes of data per hour from hundreds of thousands of sources, such as website clickstreams, financial transactions, social media feeds, IT logs, and location-tracking events. Kinesis Video Streams can continuously capture video data from smartphones, security cameras, drones, satellites, dashcams, and other edge devices.

With the [Amazon Kinesis Client Library](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html) (KCL), you can build Amazon Kinesis applications and use streaming data to power real-time dashboards, generate alerts, and implement dynamic pricing and advertising. You can also emit data from Kinesis Data Streams and Kinesis Video Streams to other AWS services such as Amazon S3, Amazon Redshift, Amazon EMR, and AWS Lambda.

Provision the level of input and output required for your data stream, in blocks of one megabyte per second (MB/sec), using the AWS Management Console, [API](https://docs.aws.amazon.com/kinesis/latest/APIReference/Welcome.html), or [[SDKs](https://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-kinesis.html)](https://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-kinesis.html). The size of your stream can be adjusted up or down at any time without restarting the stream and without any impact on the data sources pushing data to the stream. Within seconds, data put into a stream is available for analysis.

With [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/), you don't need to write applications or manage resources. You configure your data producers to send data to Firehose and it automatically delivers the data to the AWS destination or third party (Splunk) that you specified. You can also configure Firehose to transform your data before data delivery. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

 [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/) is the easiest way to process and analyze real-time, streaming data. With Managed Service for Apache Flink, you just use standard SQL or Java (Flink) to process your data streams, so you don’t have to learn any new programming languages. Simply point Managed Service for Apache Flink at an incoming data stream, write your SQL queries, and specify where you want to load the results. Managed Service for Apache Flink takes care of running your SQL queries continuously on data while it’s in transit and sending the results to the destinations.

For complex data processing applications, Amazon Managed Service for Apache Flink provides an option use open-source libraries such as Apache Flink, Apache Beam, AWS SDK, and AWS service integrations. It includes more than ten connectors from Apache Flink, and gives you the ability to build custom integrations. It’s also compatible with the [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html), a serverless feature of AWS Glue that enables you to validate and control the evolution of streaming data using registered [Apache Avro](https://avro.apache.org/) schemas.

You can use Apache Flink in Amazon Managed Service for Apache Flink to build applications whose processed records affect the results exactly once, referred to as exactly once processing. This means that even in the case of an application disruption, like internal service maintenance or user-initiated application update, the service will ensure that all data is processed and there is no duplicate data. The service stores previous and in-progress computations, or *state*, in running application storage. This enables you to compare real-time and past results over any time period, and provides fast recovery during application disruptions.

 The subsequent sections focus primarily on Amazon Kinesis Data Streams.

## Ideal usage patterns
<a name="ideal-usage-patterns-kinesis"></a>

 Amazon Kinesis Data Steams is useful wherever there is a need to move data rapidly off producers (data sources) and continuously process it. That processing can be to transform the data before emitting into another data store, drive real-time metrics and analytics, or derive and aggregate multiple streams into more complex streams, or downstream processing. The following are typical scenarios for using Kinesis Data Streams for analytics:
+  **Real-time data analytics** – Kinesis Data Streams enables real-time data analytics on streaming data, such as analyzing website clickstream data and customer engagement analytics.
+  **Log and data feed intake and processing** – With Kinesis Data Streams, you can have producers push data directly into an Amazon Kinesis stream. For example, you can submit system and application logs to Kinesis Data Streams and access the stream for processing within seconds. This prevents the log data from being lost if the front-end or application server fails, and reduces local log storage on the source. Kinesis Data Streams provides accelerated data intake because you are not batching up the data on the servers before you submit it for intake.
+  **Real-time metrics and reporting** – You can use data ingested into Kinesis Data Streams for extracting metrics and generating KPIs to power reports and dashboards at real-time speeds. This enables data-processing application logic to work on data as it is streaming in continuously, rather than waiting for data batches to arrive.

## Cost model
<a name="cost-model-kinesis"></a>

 Amazon Kinesis Data Streams has simple pay-as-you-go pricing, with no upfront costs or minimum fees, and you pay only for the resources you consume. An Amazon Kinesis stream is made up of one or more [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture)). Each shard gives you a capacity of five read transactions per second, up to a maximum total of 2 MB of data read per second. Each shard can support up to 1,000 write transactions per second, and up to a maximum total of 1 MB data written per second.

The data capacity of your stream is a function of the number of shards that you specify for the stream. The total capacity of the stream is the sum of the capacity of each shard. There are two components to pricing:
+ Primary pricing includes an hourly charge per shard and a charge for each one million PUT transactions.
+ Pricing for optional components for extended retention and enhanced fan-out.

For more information, see [Amazon Kinesis Data Streams Pricing](https://aws.amazon.com/kinesis/data-streams/pricing/). Applications that run on Amazon EC2 and process Amazon Kinesis streams also incur standard Amazon EC2 costs.

## Performance
<a name="performance-kinesis"></a>

 Amazon Kinesis Data Streams enables you to choose the throughput capacity you require in terms of shards. With each shard in an Amazon Kinesis stream, you can capture up to 1 megabyte per second of data at 1,000 write transactions per second. Your Amazon Kinesis applications can read data from each shard at up to 2 megabytes per second. You can provision as many shards as you need to get the throughput capacity you want; for example, a one gigabyte per second data stream would require 1024 shards.

Additionally, there is a new feature. [Enhanced fan-out](https://docs.amazonaws.cn/en_us/streams/latest/dev/building-enhanced-consumers-api.html) enables developers to scale up the number of stream consumers (applications reading data from a stream in real-time) by offering each stream consumer their own read throughput. Developers can register stream consumers to use enhanced fan-out and receive their own 2MB/sec pipe of read throughput per shard. This throughput automatically scales with the number of shards in a stream.

## Durability and availability
<a name="durability-and-availability-kinesis"></a>

 Amazon Kinesis Data Streams synchronously replicates data across three [Availability Zones in an AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html), providing high availability and data durability.

Additionally, you can store a cursor in Amazon DynamoDB to durably track what has been read from an Amazon Kinesis stream. In the event that your application fails in the middle of reading data from the stream, you can restart your application and use the cursor to pick up from the exact spot where the failed application left off.

## Scalability and elasticity
<a name="scalability-and-elasticity-kinesis"></a>

 You can increase or decrease the capacity of the stream at any time according to your business or operational needs, without any interruption to ongoing stream processing. By using API calls or development tools, you can automate scaling of your Amazon Kinesis Data Streams environment to meet demand and ensure you only pay for what you need.

## Interfaces
<a name="interfaces-kinesis"></a>

There are two interfaces to Kinesis Data Streams:
+ Input which is used by data producers to put data into Kinesis Data Streams
+ Output to process and analyze data that comes in

Producers can write data using the Amazon Kinesis PUT API, an [AWS Software Development Kit (SDK) or toolkit](https://aws.amazon.com/tools/) abstraction, the [Amazon Kinesis Producer Library](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-kpl.html) (KPL), or the [Amazon Kinesis Agent](https://docs.aws.amazon.com/kinesis/latest/dev/writing-with-agents.html).

For processing data that has already been put into an Amazon Kinesis stream, there are client libraries provided to build and operate real-time streaming data processing applications. The [KCL](https://github.com/awslabs/amazon-kinesis-client) acts as an intermediary between Amazon Kinesis Data Streams and your business applications which contain the specific processing logic. There is also integration to read from an Amazon Kinesis stream into [Apache Spark Streaming](https://spark.apache.org/streaming/) running on Amazon EMR.

## Anti-patterns
<a name="anti-patterns-kinesis"></a>

 Amazon Kinesis Data Streams has the following anti-patterns:
+  **Small scale consistent throughput** – Even though Kinesis Data Streams works for streaming data at 200 KB per second or less, it is designed and optimized for larger data throughputs.
+  **Long-term data storage and analytics** – Kinesis Data Streams is not suited for long-term data storage. By default, data is retained for 24 hours, and you can extend the retention period by up to 365 days.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
