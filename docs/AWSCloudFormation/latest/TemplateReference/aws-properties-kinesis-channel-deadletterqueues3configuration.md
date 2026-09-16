---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-deadletterqueues3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel DeadLetterQueueS3Configuration
<a name="aws-properties-kinesis-channel-deadletterqueues3configuration"></a>

The Amazon S3 dead-letter queue configuration for records that cannot be delivered.

## Syntax
<a name="aws-properties-kinesis-channel-deadletterqueues3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-deadletterqueues3configuration-syntax.json"></a>

```
{
  "[BucketARN](#cfn-kinesis-channel-deadletterqueues3configuration-bucketarn)" : {{String}},
  "[ErrorOutputPrefix](#cfn-kinesis-channel-deadletterqueues3configuration-erroroutputprefix)" : {{String}},
  "[ExpectedBucketOwner](#cfn-kinesis-channel-deadletterqueues3configuration-expectedbucketowner)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-deadletterqueues3configuration-syntax.yaml"></a>

```
  [BucketARN](#cfn-kinesis-channel-deadletterqueues3configuration-bucketarn): {{String}}
  [ErrorOutputPrefix](#cfn-kinesis-channel-deadletterqueues3configuration-erroroutputprefix): {{String}}
  [ExpectedBucketOwner](#cfn-kinesis-channel-deadletterqueues3configuration-expectedbucketowner): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-deadletterqueues3configuration-properties"></a>

`BucketARN`  <a name="cfn-kinesis-channel-deadletterqueues3configuration-bucketarn"></a>
The Amazon Resource Name (ARN) of the dead-letter queue Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:s3:::[a-z0-9._-]{3,63}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ErrorOutputPrefix`  <a name="cfn-kinesis-channel-deadletterqueues3configuration-erroroutputprefix"></a>
The Amazon S3 key prefix for error records.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z!\-_'.*()\/]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-kinesis-channel-deadletterqueues3configuration-expectedbucketowner"></a>
The AWS account ID of the expected owner of the dead-letter queue bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
