---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-updates.html
---

# Amazon MSK updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon MSK since this service began tracking these changes.

| Change | Description | Date |
| --- | --- | --- |
|  [WriteDataIdempotently permission added to AWSMSKReplicatorExecutionRole](security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.md) – Update to an existing policy  | Amazon MSK added WriteDataIdempotently permission to AWSMSKReplicatorExecutionRole policy to support data replication between MSK clusters. | March 12, 2024 |
|  [AWSMSKReplicatorExecutionRole](security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.md) – New policy  | Amazon MSK added AWSMSKReplicatorExecutionRole policy to support Amazon MSK Replicator. | December 4, 2023 |
|  [AmazonMSKFullAccess](security-iam-awsmanpol-AmazonMSKFullAccess.md) – Update to an existing policy  | Amazon MSK added permissions to support Amazon MSK Replicator. | September 28, 2023 |
|  [KafkaServiceRolePolicy](security-iam-awsmanpol-KafkaServiceRolePolicy.md) – Update to an existing policy  | Amazon MSK added permissions to support multi-VPC private connectivity. | March 8, 2023 |
| [AmazonMSKFullAccess](security-iam-awsmanpol-AmazonMSKFullAccess.md) – Update to an existing policy | Amazon MSK added new Amazon EC2 permissions to make it possible to connect to a cluster. | November 30, 2021 |
| [AmazonMSKFullAccess](security-iam-awsmanpol-AmazonMSKFullAccess.md) – Update to an existing policy | Amazon MSK added a new permission to allow it to describe Amazon EC2 route tables. | November 19, 2021 |
| Amazon MSK started tracking changes | Amazon MSK started tracking changes for its AWS managed policies. | November 19, 2021 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
