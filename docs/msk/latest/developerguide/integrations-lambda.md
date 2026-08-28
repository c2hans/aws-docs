---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/integrations-lambda.html
---

# AWS Lambda integration with Amazon MSK
<a name="integrations-lambda"></a>

The Lambda integration connects your Amazon MSK cluster to the selected Lambda function, using an Event Source Mapping (ESM) which constantly polls for messages in your topic using a resource called Event Poller. The ESM evaluates the message backlog – using the [OffsetLag metric](https://aws.amazon.com/blogs/compute/offset-lag-metric-for-amazon-msk-as-an-event-source-for-lambda/) – for all partitions in the topic, and auto-scales Event Pollers to process messages efficiently.

For more information, see [Using Lambda with Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html) in the *AWS Lambda Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
