---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-ts-operation-status.html
---

# Checking operation status
<a name="msk-data-delivery-s3-ts-operation-status"></a>
+ **Symptom:** You want to confirm the status of a create, update, or delete operation, or find why it failed.
+ **Resolution:** Use the `ClusterOperationArn` returned by `CreateChannel`, `UpdateChannel`, and `DeleteChannel` to look up the operation's state and any error message. Combine this with `DescribeChannel` to see the Channel's current state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
