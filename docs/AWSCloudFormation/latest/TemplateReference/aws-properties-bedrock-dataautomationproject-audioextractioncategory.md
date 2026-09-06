---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-audioextractioncategory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject AudioExtractionCategory
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategory"></a>

Settings for generating data from audio.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategory-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-audioextractioncategory-state)" : {{String}},
  "[TypeConfiguration](#cfn-bedrock-dataautomationproject-audioextractioncategory-typeconfiguration)" : {{AudioExtractionCategoryTypeConfiguration}},
  "[Types](#cfn-bedrock-dataautomationproject-audioextractioncategory-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategory-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-audioextractioncategory-state): {{String}}
  [TypeConfiguration](#cfn-bedrock-dataautomationproject-audioextractioncategory-typeconfiguration): {{
    AudioExtractionCategoryTypeConfiguration}}
  [Types](#cfn-bedrock-dataautomationproject-audioextractioncategory-types): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategory-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-audioextractioncategory-state"></a>
Whether generating categorical data from audio is enabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeConfiguration`  <a name="cfn-bedrock-dataautomationproject-audioextractioncategory-typeconfiguration"></a>
This element contains information about extractions from different types. Used to enable speaker and channel labeling for transcripts.
*Required*: No
*Type*: [AudioExtractionCategoryTypeConfiguration](aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-bedrock-dataautomationproject-audioextractioncategory-types"></a>
The types of data to generate.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
