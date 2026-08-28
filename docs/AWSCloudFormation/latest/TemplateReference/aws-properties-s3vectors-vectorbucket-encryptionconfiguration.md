---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3vectors-vectorbucket-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::VectorBucket EncryptionConfiguration
<a name="aws-properties-s3vectors-vectorbucket-encryptionconfiguration"></a>

Specifies the encryption configuration for the vector bucket. By default, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically AES256.

## Syntax
<a name="aws-properties-s3vectors-vectorbucket-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3vectors-vectorbucket-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-s3vectors-vectorbucket-encryptionconfiguration-kmskeyarn)" : {{String}},
  "[SseType](#cfn-s3vectors-vectorbucket-encryptionconfiguration-ssetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3vectors-vectorbucket-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-s3vectors-vectorbucket-encryptionconfiguration-kmskeyarn): {{String}}
  [SseType](#cfn-s3vectors-vectorbucket-encryptionconfiguration-ssetype): {{String}}
```

## Properties
<a name="aws-properties-s3vectors-vectorbucket-encryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-s3vectors-vectorbucket-encryptionconfiguration-kmskeyarn"></a>
AWS Key Management Service (KMS) customer managed key ARN to use for the encryption configuration. This parameter is required if and only if `SseType` is set to `aws:kms`.
You must specify the full ARN of the KMS key. Key IDs or key aliases aren't supported.
Amazon S3 Vectors only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SseType`  <a name="cfn-s3vectors-vectorbucket-encryptionconfiguration-ssetype"></a>
The server-side encryption type to use for the encryption configuration of the vector bucket. Valid values are `AES256` for Amazon S3 managed keys and `aws:kms` for AWS KMS keys.
*Required*: No
*Type*: String
*Allowed values*: `AES256 | aws:kms`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
