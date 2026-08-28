---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-encryption-at-rest.html
---

# Encryption at rest
<a name="next-gen-encryption-at-rest"></a>

All Next generation Resilience Hub data is encrypted at rest.

| Data store | Encryption |
| --- | --- |
| DynamoDB tables | AWS-managed keys (default) or customer-managed AWS KMS keys |
| S3 objects (topology, assessment results) | SSE-S3 (default) or SSE-KMS with customer-managed keys |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
