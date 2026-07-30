---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-audiostandardextraction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject AudioStandardExtraction
<a name="aws-properties-bedrock-dataautomationproject-audiostandardextraction"></a>

Settings for generating data from audio.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-audiostandardextraction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-audiostandardextraction-syntax.json"></a>

```
{
  "[Category](#cfn-bedrock-dataautomationproject-audiostandardextraction-category)" : {{AudioExtractionCategory}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-audiostandardextraction-syntax.yaml"></a>

```
  [Category](#cfn-bedrock-dataautomationproject-audiostandardextraction-category): {{
    AudioExtractionCategory}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-audiostandardextraction-properties"></a>

`Category`  <a name="cfn-bedrock-dataautomationproject-audiostandardextraction-category"></a>
Settings for generating data from audio.
*Required*: Yes
*Type*: [AudioExtractionCategory](aws-properties-bedrock-dataautomationproject-audioextractioncategory.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
