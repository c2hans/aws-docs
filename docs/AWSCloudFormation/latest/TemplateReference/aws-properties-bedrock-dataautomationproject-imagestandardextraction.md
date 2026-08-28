---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-imagestandardextraction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ImageStandardExtraction
<a name="aws-properties-bedrock-dataautomationproject-imagestandardextraction"></a>

Settings for generating data from images.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-imagestandardextraction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-imagestandardextraction-syntax.json"></a>

```
{
  "[BoundingBox](#cfn-bedrock-dataautomationproject-imagestandardextraction-boundingbox)" : {{ImageBoundingBox}},
  "[Category](#cfn-bedrock-dataautomationproject-imagestandardextraction-category)" : {{ImageExtractionCategory}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-imagestandardextraction-syntax.yaml"></a>

```
  [BoundingBox](#cfn-bedrock-dataautomationproject-imagestandardextraction-boundingbox): {{
    ImageBoundingBox}}
  [Category](#cfn-bedrock-dataautomationproject-imagestandardextraction-category): {{
    ImageExtractionCategory}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-imagestandardextraction-properties"></a>

`BoundingBox`  <a name="cfn-bedrock-dataautomationproject-imagestandardextraction-boundingbox"></a>
Settings for generating bounding boxes.
*Required*: Yes
*Type*: [ImageBoundingBox](aws-properties-bedrock-dataautomationproject-imageboundingbox.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Category`  <a name="cfn-bedrock-dataautomationproject-imagestandardextraction-category"></a>
Settings for generating categorical data.
*Required*: Yes
*Type*: [ImageExtractionCategory](aws-properties-bedrock-dataautomationproject-imageextractioncategory.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
