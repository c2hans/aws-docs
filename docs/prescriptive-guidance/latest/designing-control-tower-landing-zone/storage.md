---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/storage.html
---

# Storage
<a name="storage"></a>

The storage solution in the Log Archive account is implemented by using Amazon Simple Storage Service (Amazon S3). AWS Control Tower automatically sets up and manages the S3 buckets for AWS Control Tower according to AWS best practices.

The following table summarizes the storage configurations that you can configure in your landing zone. You should extend this table with additional storing solutions according to your landing zone requirements.

|
|
| Account | S3 bucket name | Description | Encryption | Lifecycle rules | Bucket policy | Created by AWS Control Tower? |
| --- |--- |--- |--- |--- |--- |--- |
| Log Archive | `aws-controltower-logs-*` | This bucket is created by AWS Control Tower and centralizes all AWS CloudTrail and AWS Config logs from all member accounts in your organization.<br />Inside the bucket, files are kept in subdirectories that use the same account ID as the directory name. | Default encryption using SSE-S3 (AES-256) | The default retention period is 1 year. You can use [AWS Control Tower customized log retention](https://aws.amazon.com/about-aws/whats-new/2022/08/aws-control-tower-customized-log-retention/) to extend log retention up to 15 years.    | Default bucket policy is applied. | Yes |
| Log Archive | `aws-controltower-s3-access-logs-*` | This bucket is created by AWS Control Tower and collects the access logs of the first `aws-controltower-logs-*` S3 bucket.                                        | Default encryption using SSE-S3 (AES-256) | The default retention period is 10 years. You can use [AWS Control Tower customized log retention](https://aws.amazon.com/about-aws/whats-new/2022/08/aws-control-tower-customized-log-retention/) to extend log retention up to 15 years.               | Default bucket policy is applied. | Yes |
| Shared Services | `aws-shared-services` | This S3 bucket is used to store the Amazon Machine Images (AMIs) for the landing zone. | Encryption using SSE-S3 (AES-256) | None. | Only accounts in the organization have access. | No |

## Encryption
<a name="encryption"></a>

Encryption is automatically enabled during landing zone setup for the S3 buckets that contain AWS Control Tower logs and access logs.

The S3 buckets for centralized logs should be encrypted at rest by using [server-side encryption with Amazon S3 managed keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html). This option encrypts each object with a unique key by using 256-bit Advanced Encryption Standard (AES-256) encryption. As an additional safeguard, Amazon S3 encrypts the key itself with a management key that it regularly rotates.

You can also use server-side encryption with AWS Key Management Service (AWS KMS) keys. For more information, see the *Server-side encryption with AWS KMS keys (SSE-KMS)* section of [Protecting data using server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) in the Amazon S3 documentation. To configure AWS Control Tower to use a customer managed key (instead of the default AWS managed key), review the section [Optionally configure AWS KMS keys](https://docs.aws.amazon.com/controltower/latest/userguide/configure-kms-keys.html) in the AWS Control Tower documentation.
