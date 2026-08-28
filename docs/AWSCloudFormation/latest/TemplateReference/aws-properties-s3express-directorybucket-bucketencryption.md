---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-bucketencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket BucketEncryption
<a name="aws-properties-s3express-directorybucket-bucketencryption"></a>

Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS). For information about default encryption for directory buckets, see [Setting and monitoring default encryption for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3express-directorybucket-bucketencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-bucketencryption-syntax.json"></a>

```
{
  "[ServerSideEncryptionConfiguration](#cfn-s3express-directorybucket-bucketencryption-serversideencryptionconfiguration)" : {{[ ServerSideEncryptionRule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-bucketencryption-syntax.yaml"></a>

```
  [ServerSideEncryptionConfiguration](#cfn-s3express-directorybucket-bucketencryption-serversideencryptionconfiguration): {{
    - ServerSideEncryptionRule}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-bucketencryption-properties"></a>

`ServerSideEncryptionConfiguration`  <a name="cfn-s3express-directorybucket-bucketencryption-serversideencryptionconfiguration"></a>
Specifies the default server-side-encryption configuration.
*Required*: Yes
*Type*: Array of [ServerSideEncryptionRule](aws-properties-s3express-directorybucket-serversideencryptionrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
