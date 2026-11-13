---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Snapshot S3PrefixLocation
<a name="aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation"></a>

Specifies an Amazon S3 bucket and key prefix.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation-syntax.json"></a>

```
{
  "[BucketARN](#cfn-kinesisanalyticsv2-snapshot-s3prefixlocation-bucketarn)" : {{String}},
  "[KeyPrefix](#cfn-kinesisanalyticsv2-snapshot-s3prefixlocation-keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation-syntax.yaml"></a>

```
  [BucketARN](#cfn-kinesisanalyticsv2-snapshot-s3prefixlocation-bucketarn): {{String}}
  [KeyPrefix](#cfn-kinesisanalyticsv2-snapshot-s3prefixlocation-keyprefix): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation-properties"></a>

`BucketARN`  <a name="cfn-kinesisanalyticsv2-snapshot-s3prefixlocation-bucketarn"></a>
The ARN of the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPrefix`  <a name="cfn-kinesisanalyticsv2-snapshot-s3prefixlocation-keyprefix"></a>
The key prefix in the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
