---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-partitions-console.html
---

# View partition information using the AWS Management Console
<a name="describe-topic-partitions-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the list of clusters, choose the name of the cluster that contains the topic.

1. On the cluster details page, choose the **Topics** tab.

1. In the list of topics, choose the name of the topic for which you want to view partition information.

1. On the topic details page, the partition information is displayed, showing the partition number, leader broker, replicas, and in-sync replicas for each partition.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
