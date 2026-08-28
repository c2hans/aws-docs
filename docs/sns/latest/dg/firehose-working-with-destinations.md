---
source_url: https://docs.aws.amazon.com/sns/latest/dg/firehose-working-with-destinations.html
---

# Managing Amazon SNS messages across multiple delivery stream destinations
<a name="firehose-working-with-destinations"></a>

[ delivery streams](sns-firehose-as-subscriber.md) allow you to manage Amazon SNS messages across multiple destinations, enabling integration with Amazon S3, Amazon OpenSearch Service, Amazon Redshift, and HTTP endpoints for storage, indexing, and analysis. By properly configuring message formatting and delivery, you can store Amazon SNS notifications in Amazon S3 for later processing, analyze structured message data using Amazon Athena, index messages in OpenSearch for real-time search and visualization, and structure archives in Amazon Redshift for advanced querying.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
