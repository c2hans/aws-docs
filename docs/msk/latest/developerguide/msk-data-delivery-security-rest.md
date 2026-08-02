---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-security-rest.html
---

# Encryption at rest
<a name="msk-data-delivery-security-rest"></a>

Data delivered to S3 (Table buckets or general-purpose buckets) is encrypted at rest using the destination bucket's default encryption settings:
+ **SSE-S3** (Amazon S3 managed keys) — default.
+ **SSE-KMS** (AWS KMS managed keys) — specify your KMS key.

If you use SSE-KMS, the Channel service role must have `kms:GenerateDataKey` and `kms:Decrypt` permissions on the specified key. For the S3 bucket destination, scope the KMS permission with the `kms:ViaService` and `kms:EncryptionContext:aws:s3:arn` conditions shown in [IAM permissions for Channel](msk-data-delivery-iam.md).

You can also set a customer-managed KMS key at the Channel level when you create the Channel, using the `encryptionConfiguration.kmsKeyArn` field.
