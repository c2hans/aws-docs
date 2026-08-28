---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/using-kms.html
---

# Using the AWS Database Encryption SDK with AWS KMS
<a name="using-kms"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

To use the AWS Database Encryption SDK, you need to configure a [keyring](keyrings.md) and specify one or more wrapping keys. If you don't have a key infrastructure, we recommend using [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/).

The AWS Database Encryption SDK supports two types of AWS KMS keyrings. The traditional [AWS KMS keyring](use-kms-keyring.md) uses [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) to generate, encrypt, and decrypt data keys. You can use either symmetric encryption (`SYMMETRIC_DEFAULT`) or asymmetric RSA KMS keys. Since the AWS Database Encryption SDK encrypts and signs every record with a unique data key, the AWS KMS keyring must call AWS KMS for every encrypt and decrypt operation. For applications that need to minimize the number of calls to AWS KMS, the AWS Database Encryption SDK also supports the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md). The Hierarchical keyring is a cryptographic materials caching solution that reduces the number of AWS KMS calls by using AWS KMS protected *branch keys* persisted in an Amazon DynamoDB table, and then locally caching branch key materials used in encrypt and decrypt operations. We recommend using the AWS KMS keyrings whenever possible.

To interact with AWS KMS, the AWS Database Encryption SDK requires the AWS KMS module of the AWS SDK for Java.

**To prepare to use the AWS Database Encryption SDK with AWS KMS**
+ Create a symmetric encryption AWS KMS key. For help, see [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
**Tip**
To use the AWS KMS key programmatically, you will need the Amazon Resource Name (ARN) of the AWS KMS key. For help finding the ARN of an AWS KMS key, see [Finding the Key ID and ARN](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn) in the *AWS Key Management Service Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
