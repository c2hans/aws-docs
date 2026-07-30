---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-videoextractioncategory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject VideoExtractionCategory
<a name="aws-properties-bedrock-dataautomationproject-videoextractioncategory"></a>

Settings for generating categorical data from video.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-videoextractioncategory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-videoextractioncategory-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-videoextractioncategory-state)" : {{String}},
  "[Types](#cfn-bedrock-dataautomationproject-videoextractioncategory-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-videoextractioncategory-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-videoextractioncategory-state): {{String}}
  [Types](#cfn-bedrock-dataautomationproject-videoextractioncategory-types): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-videoextractioncategory-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-videoextractioncategory-state"></a>
Whether generating categorical data from video is enabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-bedrock-dataautomationproject-videoextractioncategory-types"></a>
The types of data to generate.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
