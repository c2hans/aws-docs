---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-metric.html
---

# Monitor metrics
<a name="apache-iceberg-metric"></a>

For data delivery to Apache Iceberg Tables, Firehose emits the following CloudWatch metrics at a stream level.

| Metric | Description |
| --- | --- |
| DeliveryToIceberg.Bytes | The number of bytes delivered to Apache Iceberg Tables over the specified time period.<br />Units: Bytes |
| DeliveryToIceberg.IncomingRowCount | Number of records that Firehose attempts to deliver to Apache Iceberg Tables. <br />Units: Count |
| DeliveryToIceberg.SuccessfulRowCount | Number of successful rows delivered to Apache Iceberg Tables.<br />Units: Count |
| DeliveryToIceberg.FailedRowCount | Number of failed rows delivered to S3 backup bucket.<br />Units: Count |
| DeliveryToIceberg.DataFreshness | The age (from getting into Firehose to now) of the earliest record in Firehose. Any record earlier than this age has been delivered to Apache Iceberg Tables.Units: Seconds |
| DeliveryToIceberg.Success | Sum of successful commits to Apache Iceberg Tables. |
| JQProcessing.Duration | The amount of time it took to run the JQ expression.Units: Milliseconds |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
