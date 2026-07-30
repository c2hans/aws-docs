---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ImageStandardGenerativeField
<a name="aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield"></a>

Settings for generating descriptions of images.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-imagestandardgenerativefield-state)" : {{String}},
  "[Types](#cfn-bedrock-dataautomationproject-imagestandardgenerativefield-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-imagestandardgenerativefield-state): {{String}}
  [Types](#cfn-bedrock-dataautomationproject-imagestandardgenerativefield-types): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-imagestandardgenerativefield-state"></a>
Whether generating descriptions is enabled for images.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-bedrock-dataautomationproject-imagestandardgenerativefield-types"></a>
Settings for generating descriptions of images.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
