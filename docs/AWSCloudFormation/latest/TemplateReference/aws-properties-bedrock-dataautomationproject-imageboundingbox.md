---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-imageboundingbox.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ImageBoundingBox
<a name="aws-properties-bedrock-dataautomationproject-imageboundingbox"></a>

Bounding box settings for a project.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-imageboundingbox-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-imageboundingbox-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-imageboundingbox-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-imageboundingbox-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-imageboundingbox-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-imageboundingbox-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-imageboundingbox-state"></a>
Bounding box settings for a project.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
