---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-describe-topic-partitions.html
---

# View partition information for a topic
<a name="msk-describe-topic-partitions"></a>

You can retrieve detailed information about the partitions of a specific topic in your MSK Provisioned cluster. This information includes the partition number, leader broker, replica brokers, and in-sync replicas (ISR). This is useful for monitoring partition distribution, identifying under-replicated partitions, or troubleshooting replication issues.

**Note**
This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

**Topics**
+ [View partition information using the AWS Management Console](describe-topic-partitions-console.md)
+ [View partition information using the AWS CLI](describe-topic-partitions-cli.md)
+ [View partition information using the API](describe-topic-partitions-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
