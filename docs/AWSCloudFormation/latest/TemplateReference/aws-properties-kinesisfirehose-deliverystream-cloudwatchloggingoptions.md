---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream CloudWatchLoggingOptions
<a name="aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions"></a>

The `CloudWatchLoggingOptions` property type specifies Amazon CloudWatch Logs (CloudWatch Logs) logging options that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses for the delivery stream.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled)" : {{Boolean}},
  "[LogGroupName](#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname)" : {{String}},
  "[LogStreamName](#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled): {{Boolean}}
  [LogGroupName](#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname): {{String}}
  [LogStreamName](#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions-properties"></a>

`Enabled`  <a name="cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled"></a>
Indicates whether CloudWatch Logs logging is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupName`  <a name="cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname"></a>
The name of the CloudWatch Logs log group that contains the log stream that Kinesis Data Firehose will use.
Conditional. If you enable logging, you must specify this property.
*Required*: Conditional
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]*`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogStreamName`  <a name="cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname"></a>
The name of the CloudWatch Logs log stream that Kinesis Data Firehose uses to send logs about data delivery.
Conditional. If you enable logging, you must specify this property.
*Required*: Conditional
*Type*: String
*Pattern*: `[^:*]*`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
