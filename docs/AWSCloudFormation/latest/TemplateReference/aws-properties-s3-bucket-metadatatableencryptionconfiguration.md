---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metadatatableencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket MetadataTableEncryptionConfiguration
<a name="aws-properties-s3-bucket-metadatatableencryptionconfiguration"></a>

 The encryption settings for an S3 Metadata journal table or inventory table configuration.

## Syntax
<a name="aws-properties-s3-bucket-metadatatableencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-metadatatableencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-s3-bucket-metadatatableencryptionconfiguration-kmskeyarn)" : {{String}},
  "[SseAlgorithm](#cfn-s3-bucket-metadatatableencryptionconfiguration-ssealgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-metadatatableencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-s3-bucket-metadatatableencryptionconfiguration-kmskeyarn): {{String}}
  [SseAlgorithm](#cfn-s3-bucket-metadatatableencryptionconfiguration-ssealgorithm): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-metadatatableencryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-s3-bucket-metadatatableencryptionconfiguration-kmskeyarn"></a>
 If server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) is specified, you must also specify the KMS key Amazon Resource Name (ARN). You must specify a customer-managed KMS key that's located in the same Region as the general purpose bucket that corresponds to the metadata table configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SseAlgorithm`  <a name="cfn-s3-bucket-metadatatableencryptionconfiguration-ssealgorithm"></a>
 The encryption type specified for a metadata table. To specify server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), use the `aws:kms` value. To specify server-side encryption with Amazon S3 managed keys (SSE-S3), use the `AES256` value.
*Required*: Yes
*Type*: String
*Allowed values*: `aws:kms | AES256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
