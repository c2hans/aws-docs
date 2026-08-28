---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-describe-topic.html
---

# Get detailed information about a topic
<a name="msk-describe-topic"></a>

You can retrieve detailed information about a specific topic in your MSK Provisioned cluster, including its current status, partition count, replication factor, and configuration. This is useful for troubleshooting, validating topic settings, or monitoring topic status during operations.

**Note**
This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

**Topics**
+ [Describe a topic using the AWS Management Console](describe-topic-console.md)
+ [Describe a topic using the AWS CLI](describe-topic-cli.md)
+ [Describe a topic using the API](describe-topic-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
