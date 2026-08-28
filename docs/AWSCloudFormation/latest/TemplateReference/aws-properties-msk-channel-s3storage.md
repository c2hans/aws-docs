---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-s3storage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel S3Storage
<a name="aws-properties-msk-channel-s3storage"></a>

<a name="aws-properties-msk-channel-s3storage-description"></a>The `S3Storage` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-s3storage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-s3storage-syntax.json"></a>

```
{
  "[BucketArn](#cfn-msk-channel-s3storage-bucketarn)" : {{String}},
  "[CompressionType](#cfn-msk-channel-s3storage-compressiontype)" : {{String}},
  "[ExpectedBucketOwner](#cfn-msk-channel-s3storage-expectedbucketowner)" : {{String}},
  "[OutputKeyTemplate](#cfn-msk-channel-s3storage-outputkeytemplate)" : {{String}},
  "[OutputPrefix](#cfn-msk-channel-s3storage-outputprefix)" : {{String}},
  "[StorageClass](#cfn-msk-channel-s3storage-storageclass)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-channel-s3storage-syntax.yaml"></a>

```
  [BucketArn](#cfn-msk-channel-s3storage-bucketarn): {{String}}
  [CompressionType](#cfn-msk-channel-s3storage-compressiontype): {{String}}
  [ExpectedBucketOwner](#cfn-msk-channel-s3storage-expectedbucketowner): {{String}}
  [OutputKeyTemplate](#cfn-msk-channel-s3storage-outputkeytemplate): {{String}}
  [OutputPrefix](#cfn-msk-channel-s3storage-outputprefix): {{String}}
  [StorageClass](#cfn-msk-channel-s3storage-storageclass): {{String}}
```

## Properties
<a name="aws-properties-msk-channel-s3storage-properties"></a>

`BucketArn`  <a name="cfn-msk-channel-s3storage-bucketarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:s3:::.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompressionType`  <a name="cfn-msk-channel-s3storage-compressiontype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | GZIP | ZSTD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-msk-channel-s3storage-expectedbucketowner"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputKeyTemplate`  <a name="cfn-msk-channel-s3storage-outputkeytemplate"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputPrefix`  <a name="cfn-msk-channel-s3storage-outputprefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageClass`  <a name="cfn-msk-channel-s3storage-storageclass"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `STANDARD | INTELLIGENT_TIERING | GLACIER_IR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
