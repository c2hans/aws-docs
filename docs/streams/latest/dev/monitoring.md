---
source_url: https://docs.aws.amazon.com/streams/latest/dev/monitoring.html
---

# Monitor Kinesis Data Streams
<a name="monitoring"></a>

You can monitor your data streams in Amazon Kinesis Data Streams using the following features:
+ [CloudWatch metrics](monitoring-with-cloudwatch.md)— Kinesis Data Streams sends Amazon CloudWatch custom metrics with detailed monitoring for each stream.
+ [Kinesis Agent](agent-health.md)— The Kinesis Agent publishes custom CloudWatch metrics to help assess if the agent is working as expected.
+ [API logging](logging-using-cloudtrail.md)— Kinesis Data Streams uses AWS CloudTrail to log API calls and store the data in an Amazon S3 bucket.
+ [Kinesis Client Library](monitoring-with-kcl.md)— Kinesis Client Library (KCL) provides metrics per shard, worker, and KCL application.
+ [Kinesis Producer Library](monitoring-with-kpl.md)— Amazon Kinesis Producer Library (KPL) provides metrics per shard, worker, and KPL application.

For more information about common monitoring issues, questions, and troubleshooting, see the following:
+  [Which metrics should I use to monitor and troubleshoot Kinesis Data Streams issues?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-streams-troubleshoot/)
+ [Why does the IteratorAgeMilliseconds value in Kinesis Data Streams keep increasing?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-streams-iteratorage-metric/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
