---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/agent-health.html
---

# Monitor Kinesis Agent health
<a name="agent-health"></a>

Kinesis Agent publishes custom CloudWatch metrics with a namespace of **AWSKinesisAgent**. It helps assess whether the agent is healthy, submitting data into Amazon Data Firehose as specified, and consuming the appropriate amount of CPU and memory resources on the data producer.

Metrics such as number of records and bytes sent are useful to understand the rate at which the agent is submitting data to the Firehose stream. When these metrics fall below expected thresholds by some percentage or drop to zero, it could indicate configuration issues, network errors, or agent health issues. Metrics such as on-host CPU and memory consumption and agent error counters indicate data producer resource usage, and provide insights into potential configuration or host errors. Finally, the agent also logs service exceptions to help investigate agent issues.

The agent metrics are reported in the region specified in the agent configuration setting `cloudwatch.endpoint`. For more information, see [Specify agent configuration settings](agent-config-settings.md).

Cloudwatch metrics published from multiple Kinesis Agents are aggregated or combined.

There is a nominal charge for metrics emitted from Kinesis Agent, which are enabled by default. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Monitor with CloudWatch
<a name="agent-metrics"></a>

Kinesis Agent sends the following metrics to CloudWatch.

| Metric | Description |
| --- | --- |
| BytesSent | The number of bytes sent to the Firehose stream over the specified time period.<br />Units: Bytes |
| RecordSendAttempts | The number of records attempted (either first time, or as a retry) in a call to `PutRecordBatch` over the specified time period.<br />Units: Count |
| RecordSendErrors | The number of records that returned failure status in a call to `PutRecordBatch`, including retries, over the specified time period.<br />Units: Count |
| ServiceErrors | The number of calls to `PutRecordBatch` that resulted in a service error (other than a throttling error) over the specified time period. <br />Units: Count |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
