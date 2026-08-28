---
source_url: https://docs.aws.amazon.com/streams/latest/dev/using-other-services-rds.html
---

# Write to Kinesis Data Streams using Amazon Relational Database Service
<a name="using-other-services-rds"></a>

You can use Amazon Kinesis Data Streams to monitor activities on your Amazon RDS instances. Using Database Activity Streams, Amazon RDS pushes activities to a Kinesis data stream in real-time. You can then build applications for compliance management that consume these activities, audit them and generate alerts. You can also use Amazon Data Firehose to store the data.

For more information, see [Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html) in the *Amazon RDS Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
