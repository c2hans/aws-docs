---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/update-topic-cli.html
---

# Update a topic using the AWS CLI
<a name="update-topic-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster and {{TopicName}} with the name of the topic you want to update.

```
aws kafka update-topic --cluster-arn {{ClusterArn}} --topic-name {{TopicName}} --partition-count 6
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "status": "UPDATING"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
