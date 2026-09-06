---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-deadletterqueues3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel DeadLetterQueueS3
<a name="aws-properties-msk-channel-deadletterqueues3"></a>

<a name="aws-properties-msk-channel-deadletterqueues3-description"></a>The `DeadLetterQueueS3` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-deadletterqueues3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-deadletterqueues3-syntax.json"></a>

```
{
  "[BucketArn](#cfn-msk-channel-deadletterqueues3-bucketarn)" : {{String}},
  "[ErrorOutputPrefix](#cfn-msk-channel-deadletterqueues3-erroroutputprefix)" : {{String}},
  "[ExpectedBucketOwner](#cfn-msk-channel-deadletterqueues3-expectedbucketowner)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-channel-deadletterqueues3-syntax.yaml"></a>

```
  [BucketArn](#cfn-msk-channel-deadletterqueues3-bucketarn): {{String}}
  [ErrorOutputPrefix](#cfn-msk-channel-deadletterqueues3-erroroutputprefix): {{String}}
  [ExpectedBucketOwner](#cfn-msk-channel-deadletterqueues3-expectedbucketowner): {{String}}
```

## Properties
<a name="aws-properties-msk-channel-deadletterqueues3-properties"></a>

`BucketArn`  <a name="cfn-msk-channel-deadletterqueues3-bucketarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:s3:::.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ErrorOutputPrefix`  <a name="cfn-msk-channel-deadletterqueues3-erroroutputprefix"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-msk-channel-deadletterqueues3-expectedbucketowner"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
