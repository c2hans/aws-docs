---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-cloudwatchlogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel CloudWatchLogsConfiguration
<a name="aws-properties-kinesis-channel-cloudwatchlogsconfiguration"></a>

<a name="aws-properties-kinesis-channel-cloudwatchlogsconfiguration-description"></a>The `CloudWatchLogsConfiguration` property type specifies Property description not available. for an [AWS::Kinesis::Channel](aws-resource-kinesis-channel.md).

## Syntax
<a name="aws-properties-kinesis-channel-cloudwatchlogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-cloudwatchlogsconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesis-channel-cloudwatchlogsconfiguration-enabled)" : {{Boolean}},
  "[LogGroupName](#cfn-kinesis-channel-cloudwatchlogsconfiguration-loggroupname)" : {{String}},
  "[LogStreamName](#cfn-kinesis-channel-cloudwatchlogsconfiguration-logstreamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-cloudwatchlogsconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesis-channel-cloudwatchlogsconfiguration-enabled): {{Boolean}}
  [LogGroupName](#cfn-kinesis-channel-cloudwatchlogsconfiguration-loggroupname): {{String}}
  [LogStreamName](#cfn-kinesis-channel-cloudwatchlogsconfiguration-logstreamname): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-cloudwatchlogsconfiguration-properties"></a>

`Enabled`  <a name="cfn-kinesis-channel-cloudwatchlogsconfiguration-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupName`  <a name="cfn-kinesis-channel-cloudwatchlogsconfiguration-loggroupname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogStreamName`  <a name="cfn-kinesis-channel-cloudwatchlogsconfiguration-logstreamname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[^:*]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
