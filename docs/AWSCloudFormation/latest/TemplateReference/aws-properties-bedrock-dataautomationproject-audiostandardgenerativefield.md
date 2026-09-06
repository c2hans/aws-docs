---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-audiostandardgenerativefield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject AudioStandardGenerativeField
<a name="aws-properties-bedrock-dataautomationproject-audiostandardgenerativefield"></a>

Settings for generating descriptions of audio.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-audiostandardgenerativefield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-audiostandardgenerativefield-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-audiostandardgenerativefield-state)" : {{String}},
  "[Types](#cfn-bedrock-dataautomationproject-audiostandardgenerativefield-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-audiostandardgenerativefield-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-audiostandardgenerativefield-state): {{String}}
  [Types](#cfn-bedrock-dataautomationproject-audiostandardgenerativefield-types): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-audiostandardgenerativefield-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-audiostandardgenerativefield-state"></a>
Whether generating descriptions is enabled for audio.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-bedrock-dataautomationproject-audiostandardgenerativefield-types"></a>
The types of description to generate.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
