---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/streaming.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Streaming
<a name="streaming"></a>

 This stage is only applicable for real-time processing. This stage is primarily responsible for ingesting the unbounded stream of data and providing guaranteed delivery for downstream processing.

## Cost factors
<a name="streaming-cost-factors"></a>

 The primary costs of this stage are:
+  **Data transfer** – These are the costs you pay for the rate at which data is consumed by the data streaming service.
+  **Streaming service costs** – These are the costs you pay (usually per second or per hour) for AWS management of Amazon Kinesis or Amazon MSK service that is being used, including instance cost of Amazon MSK.
+  **Storage cost** – This is the cost of storing data in streaming service until data is consumed by its consumers and processed.

## Cost optimization factors
<a name="streaming-cost-optimization-factors"></a>

 Ingesting and processing real-time streaming data requires the infrastructure to support the aggregation of the source events, processing of streams, and making the data available for consumption. The AWS streaming ETL services such as Kinesis Data Streams, Kinesis Firehose, and Amazon Managed Kafka Services (MSK), reduces the administration cost. AWS manages the infrastructure, storage, networking, and configuration in your streaming ETL pipeline.

 We recommend that you consider the following actions to reduce the cost when using the following services:
+  [Kinesis Data Streams](cost-optimization-in-analytics-services.md#kinesis-data-streams)
+  [Kinesis Firehose](cost-optimization-in-analytics-services.md#id__Kinesis_Firehose)
+  [Amazon Managed Streaming for Apache Kafka(Amazon MSK)](cost-optimization-in-analytics-services.md#id__Amazon_Managed_Kafka)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
