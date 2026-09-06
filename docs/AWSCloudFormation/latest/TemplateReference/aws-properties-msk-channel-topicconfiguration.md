---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-topicconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel TopicConfiguration
<a name="aws-properties-msk-channel-topicconfiguration"></a>

<a name="aws-properties-msk-channel-topicconfiguration-description"></a>The `TopicConfiguration` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-topicconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-topicconfiguration-syntax.json"></a>

```
{
  "[RecordConverter](#cfn-msk-channel-topicconfiguration-recordconverter)" : {{RecordConverter}},
  "[RecordSchema](#cfn-msk-channel-topicconfiguration-recordschema)" : {{RecordSchema}},
  "[TopicArn](#cfn-msk-channel-topicconfiguration-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-channel-topicconfiguration-syntax.yaml"></a>

```
  [RecordConverter](#cfn-msk-channel-topicconfiguration-recordconverter): {{
    RecordConverter}}
  [RecordSchema](#cfn-msk-channel-topicconfiguration-recordschema): {{
    RecordSchema}}
  [TopicArn](#cfn-msk-channel-topicconfiguration-topicarn): {{String}}
```

## Properties
<a name="aws-properties-msk-channel-topicconfiguration-properties"></a>

`RecordConverter`  <a name="cfn-msk-channel-topicconfiguration-recordconverter"></a>
Property description not available.
*Required*: Yes
*Type*: [RecordConverter](aws-properties-msk-channel-recordconverter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordSchema`  <a name="cfn-msk-channel-topicconfiguration-recordschema"></a>
Property description not available.
*Required*: No
*Type*: [RecordSchema](aws-properties-msk-channel-recordschema.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicArn`  <a name="cfn-msk-channel-topicconfiguration-topicarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:kafka:[\w-]+:\d+:topic.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
