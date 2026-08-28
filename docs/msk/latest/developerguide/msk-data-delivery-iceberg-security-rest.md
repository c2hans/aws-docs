---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-security-rest.html
---

# Encryption at rest
<a name="msk-data-delivery-iceberg-security-rest"></a>

Data delivered to S3 Table buckets is encrypted at rest using the destination bucket's default encryption settings:
+ **SSE-S3** (Amazon S3 managed keys) — default.
+ **SSE-KMS** (AWS KMS managed keys) — specify your KMS key.

If you use SSE-KMS, the Channel service role must have `kms:GenerateDataKey` and `kms:Decrypt` permissions on the specified key. The role also needs `s3tables:PutTableEncryption` when you provide your own customer-managed KMS key (see [IAM permissions](msk-data-delivery-iceberg-iam.md)).

You can also set a customer-managed KMS key at the Channel level when you create the Channel, using the `encryptionConfiguration.kmsKeyArn` field.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
