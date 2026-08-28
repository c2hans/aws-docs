---
source_url: https://docs.aws.amazon.com/streams/latest/dev/kpl-with-firehose.html
---

# Use the KPL with Amazon Data Firehose
<a name="kpl-with-firehose"></a>

If you use the Kinesis Producer Library (KPL) to write data to a Kinesis data stream, you can use aggregation to combine the records that you write to that Kinesis data stream. If you then use that data stream as a source for your Firehose delivery stream, Firehose de-aggregates the records before it delivers them to the destination. If you configure your delivery stream to transform the data, Firehose de-aggregates the records before it delivers them to AWS Lambda. For more information, see [Writing to Amazon Firehose Using Kinesis Data Streams](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-kinesis-streams.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
