---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaConnectRouterOutputConnectionMap
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap"></a>

A map of output names to the MediaConnect Router connection for this pipeline. Only present for channels with MediaConnect Router outputs.

## Syntax
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap-syntax.json"></a>

```
{
  "[Pipeline0](#cfn-medialive-channel-mediaconnectrouteroutputconnectionmap-pipeline0)" : {{String}},
  "[Pipeline1](#cfn-medialive-channel-mediaconnectrouteroutputconnectionmap-pipeline1)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap-syntax.yaml"></a>

```
  [Pipeline0](#cfn-medialive-channel-mediaconnectrouteroutputconnectionmap-pipeline0): {{String}}
  [Pipeline1](#cfn-medialive-channel-mediaconnectrouteroutputconnectionmap-pipeline1): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap-properties"></a>

`Pipeline0`  <a name="cfn-medialive-channel-mediaconnectrouteroutputconnectionmap-pipeline0"></a>
The ARN of the MediaConnect Router Input connected to pipeline 0.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pipeline1`  <a name="cfn-medialive-channel-mediaconnectrouteroutputconnectionmap-pipeline1"></a>
The ARN of the MediaConnect Router Input connected to pipeline 1.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
