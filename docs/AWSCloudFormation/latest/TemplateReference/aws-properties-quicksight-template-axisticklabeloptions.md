---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-axisticklabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template AxisTickLabelOptions
<a name="aws-properties-quicksight-template-axisticklabeloptions"></a>

The tick label options of an axis.

## Syntax
<a name="aws-properties-quicksight-template-axisticklabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-axisticklabeloptions-syntax.json"></a>

```
{
  "[LabelOptions](#cfn-quicksight-template-axisticklabeloptions-labeloptions)" : {{LabelOptions}},
  "[RotationAngle](#cfn-quicksight-template-axisticklabeloptions-rotationangle)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-axisticklabeloptions-syntax.yaml"></a>

```
  [LabelOptions](#cfn-quicksight-template-axisticklabeloptions-labeloptions): {{
    LabelOptions}}
  [RotationAngle](#cfn-quicksight-template-axisticklabeloptions-rotationangle): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-axisticklabeloptions-properties"></a>

`LabelOptions`  <a name="cfn-quicksight-template-axisticklabeloptions-labeloptions"></a>
Determines whether or not the axis ticks are visible.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-template-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RotationAngle`  <a name="cfn-quicksight-template-axisticklabeloptions-rotationangle"></a>
The rotation angle of the axis tick labels.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
