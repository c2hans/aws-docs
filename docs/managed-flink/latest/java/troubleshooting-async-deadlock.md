---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-async-deadlock.html
---

# Flink 1.15 Async Sink Deadlock
<a name="troubleshooting-async-deadlock"></a>

There is a [known issue](https://issues.apache.org/jira/browse/FLINK-32230) with AWS connectors for Apache Flink implementing AsyncSink interface. This affects applications using Flink 1.15 with the following connectors:
+ For Java applications:
  + KinesisStreamsSink – `org.apache.flink:flink-connector-kinesis`
  + KinesisStreamsSink – `org.apache.flink:flink-connector-aws-kinesis-streams`
  + KinesisFirehoseSink – `org.apache.flink:flink-connector-aws-kinesis-firehose`
  + DynamoDbSink – `org.apache.flink:flink-connector-dynamodb`
+ Flink SQL/TableAPI/Python applications:
  + kinesis – `org.apache.flink:flink-sql-connector-kinesis`
  + kinesis – `org.apache.flink:flink-sql-connector-aws-kinesis-streams`
  + firehose – `org.apache.flink:flink-sql-connector-aws-kinesis-firehose`
  + dynamodb – `org.apache.flink:flink-sql-connector-dynamodb`

Affected applications will experience the following symptoms:
+ Flink job is in `RUNNING` state, but not processing data;
+ There are no job restarts;
+ Checkpoints are timing out.

The issue is caused by a [bug](https://github.com/aws/aws-sdk-java-v2/issues/4354) in AWS SDK resulting in it not surfacing certain errors to the caller when using the async HTTP client. This results in the sink waiting indefinitely for an “in-flight request” to complete during a checkpoint flush operation.

This issue had been fixed in AWS SDK starting from version **2.20.144**.

Following are instructions on how to update affected connectors to use the new version of AWS SDK in your applications:

**Topics**
+ [Update Java applications](troubleshooting-async-deadlock-update-java-apps.md)
+ [Update Python applications](troubleshooting-async-deadlock-update-python-apps.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
