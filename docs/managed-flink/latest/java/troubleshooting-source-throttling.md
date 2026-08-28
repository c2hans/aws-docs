---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-source-throttling.html
---

# Upstream or source throttling from a Kinesis data stream
<a name="troubleshooting-source-throttling"></a>

**Symptom**: The application is encountering `LimitExceededExceptions` from their upstream source Kinesis data stream.

**Potential Cause**: The default setting for the Apache Flink library Kinesis connector is set to read from the Kinesis data stream source with a very aggressive default setting for the maximum number of records fetched per `GetRecords` call. Apache Flink is configured by default to fetch 10,000 records per `GetRecords` call (this call is made by default every 200 ms), although the limit per shard is only 1,000 records.

This default behavior can lead to throttling when attempting to consume from the Kinesis data stream, which will affect the applications performance and stability.

You can confirm this by checking the CloudWatch `ReadProvisionedThroughputExceeded` metric and seeing prolonged or sustained periods where this metric is greater than zero.

You can also see this in CloudWatch logs for your Amazon Managed Service for Apache Flink application by observing continued `LimitExceededException` errors.

**Resolution**: You can do one of two things to resolve this scenario:
+ Lower the default limit for the number of records fetched per `GetRecords` call
+ Enable Adaptive Reads in your Amazon Managed Service for Apache Flink application. For more information on the Adaptive Reads feature, see [SHARD\_USE\_ADAPTIVE\_READS](https://nightlies.apache.org/flink/flink-docs-release-1.10/api/java/org/apache/flink/streaming/connectors/kinesis/config/ConsumerConfigConstants.html#SHARD_USE_ADAPTIVE_READS)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
