---
source_url: https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html
---

# Read data from Amazon Kinesis Data Streams
<a name="building-consumers"></a>

A *consumer* is an application that processes all data from a Kinesis data stream. When a consumer uses *enhanced fan-out*, it gets its own 2 MB/sec allotment of read throughput, allowing multiple consumers to read data from the same stream in parallel, without contending for read throughput with other consumers. To use the enhanced fan-out capability of shards, see [Develop enhanced fan-out consumers with dedicated throughput](enhanced-consumers.md).

You can build consumers for Kinesis Data Streams using Kinesis Client Library (KCL) or AWS SDK for Java. You can also develop consumers using other AWS services such as AWS Lambda, Amazon Managed Service for Apache Flink, and Amazon Data Firehose. Kinesis Data Streams supports integrations with other AWS services such as Amazon EMR, Amazon EventBridge, AWS Glue, and Amazon Redshift. It also supports third party integrations including Apache Flink, Adobe Experience Platform, Apache Druid, Apache Spark, Databricks, Confluent Platform, Kinesumer, and Talend.

**Topics**
+ [Develop enhanced fan-out consumers with dedicated throughput](enhanced-consumers.md)
+ [Use the Data Viewer in the Kinesis console](data-viewer.md)
+ [Query your data streams in the Kinesis console](querying-data.md)
+ [Use Kinesis Client Library](kcl.md)
+ [Develop consumers with the AWS SDK for Java](develop-consumers-sdk.md)
+ [Develop consumers using AWS Lambda](lambda-consumer.md)
+ [Develop consumers using Amazon Managed Service for Apache Flink](kda-consumer.md)
+ [Develop consumers using Amazon Data Firehose](kdf-consumer.md)
+ [Read data from Kinesis Data Streams using other AWS services](using-other-services-read.md)
+ [Read from Kinesis Data Streams using third-party integrations](using-services-third-party-read.md)
+ [Troubleshoot Kinesis Data Streams consumers](troubleshooting-consumers.md)
+ [Optimize Amazon Kinesis Data Streams consumers](advanced-consumers.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
