---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-topic.html
---

# Update a topic in an Amazon MSK cluster
<a name="msk-update-topic"></a>

Update the partition count or topic-level configurations for an existing topic. This operation modifies the topic without requiring recreation.

**Note**
You can update either the partition count or the topic configurations in a single API call, but not both simultaneously. To update both, make separate API calls.

**Topics**
+ [Update a topic using the AWS Management Console](update-topic-console.md)
+ [Update a topic using the AWS CLI](update-topic-cli.md)
+ [Update a topic using the API](update-topic-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
