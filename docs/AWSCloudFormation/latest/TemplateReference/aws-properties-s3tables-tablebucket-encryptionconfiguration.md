---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket EncryptionConfiguration
<a name="aws-properties-s3tables-tablebucket-encryptionconfiguration"></a>

Configuration specifying how data should be encrypted. This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.

## Syntax
<a name="aws-properties-s3tables-tablebucket-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-encryptionconfiguration-syntax.json"></a>

```
{
  "[KMSKeyArn](#cfn-s3tables-tablebucket-encryptionconfiguration-kmskeyarn)" : {{String}},
  "[SSEAlgorithm](#cfn-s3tables-tablebucket-encryptionconfiguration-ssealgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-encryptionconfiguration-syntax.yaml"></a>

```
  [KMSKeyArn](#cfn-s3tables-tablebucket-encryptionconfiguration-kmskeyarn): {{String}}
  [SSEAlgorithm](#cfn-s3tables-tablebucket-encryptionconfiguration-ssealgorithm): {{String}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-encryptionconfiguration-properties"></a>

`KMSKeyArn`  <a name="cfn-s3tables-tablebucket-encryptionconfiguration-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key to use for encryption. This field is required only when `sseAlgorithm` is set to `aws:kms`.
*Required*: No
*Type*: String
*Pattern*: `(arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+)`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSEAlgorithm`  <a name="cfn-s3tables-tablebucket-encryptionconfiguration-ssealgorithm"></a>
The server-side encryption algorithm to use. Valid values are `AES256` for S3-managed encryption keys, or `aws:kms` for AWS KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html).
*Required*: No
*Type*: String
*Allowed values*: `AES256 | aws:kms`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
