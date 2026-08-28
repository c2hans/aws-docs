---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-bucketencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket BucketEncryption
<a name="aws-properties-s3-bucket-bucketencryption"></a>

Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3), AWS KMS-managed keys (SSE-KMS), or dual-layer server-side encryption with KMS-managed keys (DSSE-KMS). For information about the Amazon S3 default encryption feature, see [Amazon S3 Default Encryption for S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3-bucket-bucketencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-bucketencryption-syntax.json"></a>

```
{
  "[ServerSideEncryptionConfiguration](#cfn-s3-bucket-bucketencryption-serversideencryptionconfiguration)" : {{[ ServerSideEncryptionRule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3-bucket-bucketencryption-syntax.yaml"></a>

```
  [ServerSideEncryptionConfiguration](#cfn-s3-bucket-bucketencryption-serversideencryptionconfiguration): {{
    - ServerSideEncryptionRule}}
```

## Properties
<a name="aws-properties-s3-bucket-bucketencryption-properties"></a>

`ServerSideEncryptionConfiguration`  <a name="cfn-s3-bucket-bucketencryption-serversideencryptionconfiguration"></a>
Specifies the default server-side-encryption configuration.
*Required*: Yes
*Type*: Array of [ServerSideEncryptionRule](aws-properties-s3-bucket-serversideencryptionrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-s3-bucket-bucketencryption--seealso"></a>
+ AWS::S3::Bucket [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#aws-properties-s3-bucket--examples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
