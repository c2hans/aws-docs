---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentboundingbox.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentBoundingBox
<a name="aws-properties-bedrock-dataautomationproject-documentboundingbox"></a>

Bounding box settings for documents.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentboundingbox-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentboundingbox-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-documentboundingbox-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentboundingbox-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-documentboundingbox-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentboundingbox-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-documentboundingbox-state"></a>
Whether bounding boxes are enabled for documents.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
