---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-s3destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel S3DestinationConfiguration
<a name="aws-properties-kinesis-channel-s3destinationconfiguration"></a>

The configuration for delivery to a general purpose Amazon S3 bucket. Used in CreateChannel.

## Syntax
<a name="aws-properties-kinesis-channel-s3destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-s3destinationconfiguration-syntax.json"></a>

```
{
  "[DataFreshnessInSeconds](#cfn-kinesis-channel-s3destinationconfiguration-datafreshnessinseconds)" : {{Integer}},
  "[DeadLetterQueueS3Configuration](#cfn-kinesis-channel-s3destinationconfiguration-deadletterqueues3configuration)" : {{DeadLetterQueueS3Configuration}},
  "[StorageConfiguration](#cfn-kinesis-channel-s3destinationconfiguration-storageconfiguration)" : {{S3StorageConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-s3destinationconfiguration-syntax.yaml"></a>

```
  [DataFreshnessInSeconds](#cfn-kinesis-channel-s3destinationconfiguration-datafreshnessinseconds): {{Integer}}
  [DeadLetterQueueS3Configuration](#cfn-kinesis-channel-s3destinationconfiguration-deadletterqueues3configuration): {{
    DeadLetterQueueS3Configuration}}
  [StorageConfiguration](#cfn-kinesis-channel-s3destinationconfiguration-storageconfiguration): {{
    S3StorageConfiguration}}
```

## Properties
<a name="aws-properties-kinesis-channel-s3destinationconfiguration-properties"></a>

`DataFreshnessInSeconds`  <a name="cfn-kinesis-channel-s3destinationconfiguration-datafreshnessinseconds"></a>
The maximum age, in seconds, of undelivered data before the channel delivers it to the destination. The default value is 300 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterQueueS3Configuration`  <a name="cfn-kinesis-channel-s3destinationconfiguration-deadletterqueues3configuration"></a>
The dead-letter queue configuration for records that cannot be delivered. Optional for general purpose Amazon S3 destinations. If not specified, it defaults to the destination bucket with an error prefix.
*Required*: No
*Type*: [DeadLetterQueueS3Configuration](aws-properties-kinesis-channel-deadletterqueues3configuration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageConfiguration`  <a name="cfn-kinesis-channel-s3destinationconfiguration-storageconfiguration"></a>
The Amazon S3 storage configuration for the channel.
*Required*: Yes
*Type*: [S3StorageConfiguration](aws-properties-kinesis-channel-s3storageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
