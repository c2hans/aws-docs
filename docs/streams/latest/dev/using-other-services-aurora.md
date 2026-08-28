---
source_url: https://docs.aws.amazon.com/streams/latest/dev/using-other-services-aurora.html
---

# Write to Kinesis Data Streams using Amazon Aurora
<a name="using-other-services-aurora"></a>

You can use Amazon Kinesis Data Streams to monitor activities on your Amazon Aurora DB clusters. Using Database Activity Streams, your Aurora DB cluster pushes activities to an Amazon Kinesis Data Stream in real-time. You can then build applications for compliance management that consume these activities, audit them and generate alerts. You can also use Amazon Amazon Firehose to store the data.

For more information, see [Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html) in the *Amazon Aurora Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
