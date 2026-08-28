---
source_url: https://docs.aws.amazon.com/sns/latest/dg/firehose-s3-destinations.html
---

# Storing and analyzing Amazon SNS messages in Amazon S3 destinations
<a name="firehose-s3-destinations"></a>

This topic explains how delivery streams publish data to Amazon Simple Storage Service (Amazon S3).

![The integration and workflow of Amazon services for message handling. It shows how a publisher sends messages to an Amazon SNS topic, which then fans out messages to multiple Amazon SQS queues and an Data Firehose delivery stream. From there, messages can be processed by Lambda functions or stored persistently in an Amazon S3 bucket.](http://docs.aws.amazon.com/sns/latest/dg/images/firehose-architecture-s3.png)

**Topics**
+ [Formatting notifications for storage in Amazon S3 destinations](firehose-archived-message-format-S3.md)
+ [Analyzing messages stored in Amazon S3 using Athena](firehose-message-analysis-s3.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
