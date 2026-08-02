---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialgradientstepcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialGradientStepColor
<a name="aws-properties-quicksight-analysis-geospatialgradientstepcolor"></a>

The gradient step color for a single step.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialgradientstepcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialgradientstepcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-geospatialgradientstepcolor-color)" : {{String}},
  "[DataValue](#cfn-quicksight-analysis-geospatialgradientstepcolor-datavalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialgradientstepcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-geospatialgradientstepcolor-color): {{String}}
  [DataValue](#cfn-quicksight-analysis-geospatialgradientstepcolor-datavalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialgradientstepcolor-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-geospatialgradientstepcolor-color"></a>
The color and opacity values for the gradient step color.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-analysis-geospatialgradientstepcolor-datavalue"></a>
The data value for the gradient step color.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
