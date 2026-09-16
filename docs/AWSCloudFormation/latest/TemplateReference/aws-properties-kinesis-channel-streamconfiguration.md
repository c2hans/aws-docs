---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-streamconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel StreamConfiguration
<a name="aws-properties-kinesis-channel-streamconfiguration"></a>

<a name="aws-properties-kinesis-channel-streamconfiguration-description"></a>The `StreamConfiguration` property type specifies Property description not available. for an [AWS::Kinesis::Channel](aws-resource-kinesis-channel.md).

## Syntax
<a name="aws-properties-kinesis-channel-streamconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-streamconfiguration-syntax.json"></a>

```
{
  "[RecordConfiguration](#cfn-kinesis-channel-streamconfiguration-recordconfiguration)" : {{RecordConfiguration}},
  "[StreamARN](#cfn-kinesis-channel-streamconfiguration-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-streamconfiguration-syntax.yaml"></a>

```
  [RecordConfiguration](#cfn-kinesis-channel-streamconfiguration-recordconfiguration): {{
    RecordConfiguration}}
  [StreamARN](#cfn-kinesis-channel-streamconfiguration-streamarn): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-streamconfiguration-properties"></a>

`RecordConfiguration`  <a name="cfn-kinesis-channel-streamconfiguration-recordconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [RecordConfiguration](aws-properties-kinesis-channel-recordconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamARN`  <a name="cfn-kinesis-channel-streamconfiguration-streamarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
