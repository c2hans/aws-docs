---
source_url: https://docs.aws.amazon.com/sns/latest/dg/firehose-http-destinations.html
---

# Configuring Amazon SNS message delivery to HTTP destinations using
<a name="firehose-http-destinations"></a>

This topic explains how delivery streams publish data to HTTP endpoints.

![A publisher to an Amazon SNS topic, which then distributes the messages to multiple Amazon SQS queues. These messages are processed by Lambda functions and also sent through an Data Firehose delivery stream to an HTTP endpoint. This setup showcases how AWS services work together to facilitate message handling and integration with external HTTP services.](http://docs.aws.amazon.com/sns/latest/dg/images/firehose-architecture-http.png)

**Topics**
+ [Notification format for delivery to HTTP destinations](firehose-delivered-message-format-http.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
