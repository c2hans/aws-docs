---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-s3storageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel S3StorageConfiguration
<a name="aws-properties-kinesis-channel-s3storageconfiguration"></a>

The Amazon S3 storage settings for a general purpose Amazon S3 destination.

## Syntax
<a name="aws-properties-kinesis-channel-s3storageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-s3storageconfiguration-syntax.json"></a>

```
{
  "[BucketARN](#cfn-kinesis-channel-s3storageconfiguration-bucketarn)" : {{String}},
  "[CompressionType](#cfn-kinesis-channel-s3storageconfiguration-compressiontype)" : {{String}},
  "[ExpectedBucketOwner](#cfn-kinesis-channel-s3storageconfiguration-expectedbucketowner)" : {{String}},
  "[OutputKeyTemplate](#cfn-kinesis-channel-s3storageconfiguration-outputkeytemplate)" : {{String}},
  "[StorageClass](#cfn-kinesis-channel-s3storageconfiguration-storageclass)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-s3storageconfiguration-syntax.yaml"></a>

```
  [BucketARN](#cfn-kinesis-channel-s3storageconfiguration-bucketarn): {{String}}
  [CompressionType](#cfn-kinesis-channel-s3storageconfiguration-compressiontype): {{String}}
  [ExpectedBucketOwner](#cfn-kinesis-channel-s3storageconfiguration-expectedbucketowner): {{String}}
  [OutputKeyTemplate](#cfn-kinesis-channel-s3storageconfiguration-outputkeytemplate): {{String}}
  [StorageClass](#cfn-kinesis-channel-s3storageconfiguration-storageclass): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-s3storageconfiguration-properties"></a>

`BucketARN`  <a name="cfn-kinesis-channel-s3storageconfiguration-bucketarn"></a>
The Amazon Resource Name (ARN) of the destination Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:s3:::[a-z0-9._-]{3,63}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompressionType`  <a name="cfn-kinesis-channel-s3storageconfiguration-compressiontype"></a>
The compression applied to delivered objects. Valid values:
+ `NONE` - No compression.
+ `GZIP` - gzip compression.
+ `ZSTD` - Zstandard compression.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | GZIP | ZSTD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-kinesis-channel-s3storageconfiguration-expectedbucketowner"></a>
The AWS account ID of the expected owner of the destination bucket. This value helps prevent delivery to an unintended bucket if ownership changes.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputKeyTemplate`  <a name="cfn-kinesis-channel-s3storageconfiguration-outputkeytemplate"></a>
The template used to construct the Amazon S3 object key for delivered objects. If not specified, a default template is used.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z!\-_'.*()\/=:{}]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageClass`  <a name="cfn-kinesis-channel-s3storageconfiguration-storageclass"></a>
The Amazon S3 storage class for delivered objects. Valid values:
+ `STANDARD` - The default storage class, for frequently accessed data.
+ `INTELLIGENT_TIERING` - Automatically moves objects to the most cost-effective access tier based on usage patterns.
+ `GLACIER_IR` - Low-cost storage for rarely accessed data that requires millisecond retrieval.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | INTELLIGENT_TIERING | GLACIER_IR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
