---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentstandardextraction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentStandardExtraction
<a name="aws-properties-bedrock-dataautomationproject-documentstandardextraction"></a>

Settings for generating data from documents.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentstandardextraction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentstandardextraction-syntax.json"></a>

```
{
  "[BoundingBox](#cfn-bedrock-dataautomationproject-documentstandardextraction-boundingbox)" : {{DocumentBoundingBox}},
  "[Granularity](#cfn-bedrock-dataautomationproject-documentstandardextraction-granularity)" : {{DocumentExtractionGranularity}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentstandardextraction-syntax.yaml"></a>

```
  [BoundingBox](#cfn-bedrock-dataautomationproject-documentstandardextraction-boundingbox): {{
    DocumentBoundingBox}}
  [Granularity](#cfn-bedrock-dataautomationproject-documentstandardextraction-granularity): {{
    DocumentExtractionGranularity}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentstandardextraction-properties"></a>

`BoundingBox`  <a name="cfn-bedrock-dataautomationproject-documentstandardextraction-boundingbox"></a>
Whether to generate bounding boxes.
*Required*: Yes
*Type*: [DocumentBoundingBox](aws-properties-bedrock-dataautomationproject-documentboundingbox.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Granularity`  <a name="cfn-bedrock-dataautomationproject-documentstandardextraction-granularity"></a>
Which granularities to generate data for.
*Required*: Yes
*Type*: [DocumentExtractionGranularity](aws-properties-bedrock-dataautomationproject-documentextractiongranularity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
