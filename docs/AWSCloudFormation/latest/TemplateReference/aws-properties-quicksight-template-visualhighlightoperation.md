---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-visualhighlightoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template VisualHighlightOperation
<a name="aws-properties-quicksight-template-visualhighlightoperation"></a>

Defines what initiates a highlight operation on a visual, such as a click or hover.

## Syntax
<a name="aws-properties-quicksight-template-visualhighlightoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-visualhighlightoperation-syntax.json"></a>

```
{
  "[Trigger](#cfn-quicksight-template-visualhighlightoperation-trigger)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-visualhighlightoperation-syntax.yaml"></a>

```
  [Trigger](#cfn-quicksight-template-visualhighlightoperation-trigger): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-visualhighlightoperation-properties"></a>

`Trigger`  <a name="cfn-quicksight-template-visualhighlightoperation-trigger"></a>
Specifies whether a highlight operation is initiated by a click or hover, or whether it's disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `DATA_POINT_CLICK | DATA_POINT_HOVER | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
