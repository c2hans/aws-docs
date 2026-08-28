---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3vectors-index-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::Index EncryptionConfiguration
<a name="aws-properties-s3vectors-index-encryptionconfiguration"></a>

The encryption configuration for a vector bucket or index. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically `AES256`. You can optionally override bucket level encryption settings, and set a specific encryption configuration for a vector index at the time of index creation.

## Syntax
<a name="aws-properties-s3vectors-index-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3vectors-index-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-s3vectors-index-encryptionconfiguration-kmskeyarn)" : {{String}},
  "[SseType](#cfn-s3vectors-index-encryptionconfiguration-ssetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3vectors-index-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-s3vectors-index-encryptionconfiguration-kmskeyarn): {{String}}
  [SseType](#cfn-s3vectors-index-encryptionconfiguration-ssetype): {{String}}
```

## Properties
<a name="aws-properties-s3vectors-index-encryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-s3vectors-index-encryptionconfiguration-kmskeyarn"></a>
AWS Key Management Service (KMS) customer managed key ID to use for the encryption configuration. This parameter is allowed if and only if `sseType` is set to `aws:kms`.
To specify the KMS key, you must use the format of the KMS key Amazon Resource Name (ARN).
For example, specify Key ARN in the following format: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SseType`  <a name="cfn-s3vectors-index-encryptionconfiguration-ssetype"></a>
The server-side encryption type to use for the encryption configuration of the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically `AES256`.
*Required*: No
*Type*: String
*Allowed values*: `AES256 | aws:kms`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
