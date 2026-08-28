---
source_url: https://docs.aws.amazon.com/streams/latest/dev/using-other-services-ddb.html
---

# Write to Kinesis Data Streams using Amazon DynamoDB
<a name="using-other-services-ddb"></a>

You can use Amazon Kinesis Data Streams to capture changes to Amazon DynamoDB. Kinesis Data Streams captures item-level modifications in any DynamoDB table and replicates them to a Kinesis data stream. Your consumer applications can access this stream to view item-level changes in real time and deliver those changes downstream or take action based on the content.

For more information, see [how Kinesis Data Streams work with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds.html) in the *Amazon DynamoDB Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
