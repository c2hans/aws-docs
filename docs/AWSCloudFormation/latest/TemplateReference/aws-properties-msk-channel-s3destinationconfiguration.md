---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-s3destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel S3DestinationConfiguration
<a name="aws-properties-msk-channel-s3destinationconfiguration"></a>

<a name="aws-properties-msk-channel-s3destinationconfiguration-description"></a>The `S3DestinationConfiguration` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-s3destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-s3destinationconfiguration-syntax.json"></a>

```
{
  "[DataFreshnessInSeconds](#cfn-msk-channel-s3destinationconfiguration-datafreshnessinseconds)" : {{Integer}},
  "[DeadLetterQueueS3](#cfn-msk-channel-s3destinationconfiguration-deadletterqueues3)" : {{DeadLetterQueueS3}},
  "[ServiceExecutionRoleArn](#cfn-msk-channel-s3destinationconfiguration-serviceexecutionrolearn)" : {{String}},
  "[Storage](#cfn-msk-channel-s3destinationconfiguration-storage)" : {{S3Storage}}
}
```

### YAML
<a name="aws-properties-msk-channel-s3destinationconfiguration-syntax.yaml"></a>

```
  [DataFreshnessInSeconds](#cfn-msk-channel-s3destinationconfiguration-datafreshnessinseconds): {{Integer}}
  [DeadLetterQueueS3](#cfn-msk-channel-s3destinationconfiguration-deadletterqueues3): {{
    DeadLetterQueueS3}}
  [ServiceExecutionRoleArn](#cfn-msk-channel-s3destinationconfiguration-serviceexecutionrolearn): {{String}}
  [Storage](#cfn-msk-channel-s3destinationconfiguration-storage): {{
    S3Storage}}
```

## Properties
<a name="aws-properties-msk-channel-s3destinationconfiguration-properties"></a>

`DataFreshnessInSeconds`  <a name="cfn-msk-channel-s3destinationconfiguration-datafreshnessinseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterQueueS3`  <a name="cfn-msk-channel-s3destinationconfiguration-deadletterqueues3"></a>
Property description not available.
*Required*: Yes
*Type*: [DeadLetterQueueS3](aws-properties-msk-channel-deadletterqueues3.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceExecutionRoleArn`  <a name="cfn-msk-channel-s3destinationconfiguration-serviceexecutionrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:iam::[\w-]+:role.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Storage`  <a name="cfn-msk-channel-s3destinationconfiguration-storage"></a>
Property description not available.
*Required*: Yes
*Type*: [S3Storage](aws-properties-msk-channel-s3storage.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
