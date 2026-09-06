---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ImageStandardOutputConfiguration
<a name="aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration"></a>

Output settings for processing images.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration-syntax.json"></a>

```
{
  "[Extraction](#cfn-bedrock-dataautomationproject-imagestandardoutputconfiguration-extraction)" : {{ImageStandardExtraction}},
  "[GenerativeField](#cfn-bedrock-dataautomationproject-imagestandardoutputconfiguration-generativefield)" : {{ImageStandardGenerativeField}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration-syntax.yaml"></a>

```
  [Extraction](#cfn-bedrock-dataautomationproject-imagestandardoutputconfiguration-extraction): {{
    ImageStandardExtraction}}
  [GenerativeField](#cfn-bedrock-dataautomationproject-imagestandardoutputconfiguration-generativefield): {{
    ImageStandardGenerativeField}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration-properties"></a>

`Extraction`  <a name="cfn-bedrock-dataautomationproject-imagestandardoutputconfiguration-extraction"></a>
Settings for populating data fields that describe the image.
*Required*: No
*Type*: [ImageStandardExtraction](aws-properties-bedrock-dataautomationproject-imagestandardextraction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenerativeField`  <a name="cfn-bedrock-dataautomationproject-imagestandardoutputconfiguration-generativefield"></a>
Whether to generate descriptions of the data.
*Required*: No
*Type*: [ImageStandardGenerativeField](aws-properties-bedrock-dataautomationproject-imagestandardgenerativefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
