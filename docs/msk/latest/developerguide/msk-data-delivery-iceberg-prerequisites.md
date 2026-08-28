---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-prerequisites.html
---

# Prerequisites
<a name="msk-data-delivery-iceberg-prerequisites"></a>

1. An Amazon MSK Provisioned cluster with Express brokers.

1. A Kafka topic producing data in a supported format for your destination.

1. An S3 bucket for the dead-letter queue (DLQ) — **required**.

1. An IAM service role (see [IAM permissions](msk-data-delivery-iceberg-iam.md)).

1. A schema registered in AWS Glue Schema Registry that matches the topic data, and an S3 Table bucket in the same AWS Region as the cluster.

1. (Optional) A customer-managed KMS key for encryption at rest.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
