---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-iam-lifecycle.html
---

# Channel lifecycle management permissions
<a name="msk-data-delivery-iceberg-iam-lifecycle"></a>

The following permissions are for the IAM principal (the user or role) you use to create, update, describe, delete, and list Channels. They are not part of the service execution role.

| API action | Required permission | Resource |
| --- | --- | --- |
| CreateChannel | `kafka:CreateChannel` | Cluster ARN |
| DescribeChannel | `kafka:DescribeChannel` | Channel ARN |
| UpdateChannel | `kafka:UpdateChannel` | Channel ARN |
| DeleteChannel | `kafka:DeleteChannel` | Channel ARN |
| ListChannels | `kafka:ListChannels` | Cluster ARN |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
