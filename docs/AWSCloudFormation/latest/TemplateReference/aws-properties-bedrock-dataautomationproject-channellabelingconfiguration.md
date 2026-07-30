---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-channellabelingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ChannelLabelingConfiguration
<a name="aws-properties-bedrock-dataautomationproject-channellabelingconfiguration"></a>

Enables or disables channel labeling. Channel labeling, when enabled will assign a number to each audio channel, and indicate which channel is being used in each portion of the transcript. This appears in the response as "ch\_0" for the first channel, and "ch\_1" for the second.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-channellabelingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-channellabelingconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-channellabelingconfiguration-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-channellabelingconfiguration-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-channellabelingconfiguration-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-channellabelingconfiguration-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-channellabelingconfiguration-state"></a>
State of channel labeling, either enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
