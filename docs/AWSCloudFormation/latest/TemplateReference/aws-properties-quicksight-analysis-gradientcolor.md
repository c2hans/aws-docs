---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-gradientcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GradientColor
<a name="aws-properties-quicksight-analysis-gradientcolor"></a>

Determines the gradient color settings.

## Syntax
<a name="aws-properties-quicksight-analysis-gradientcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-gradientcolor-syntax.json"></a>

```
{
  "[Stops](#cfn-quicksight-analysis-gradientcolor-stops)" : {{[ GradientStop, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-gradientcolor-syntax.yaml"></a>

```
  [Stops](#cfn-quicksight-analysis-gradientcolor-stops): {{
    - GradientStop}}
```

## Properties
<a name="aws-properties-quicksight-analysis-gradientcolor-properties"></a>

`Stops`  <a name="cfn-quicksight-analysis-gradientcolor-stops"></a>
The list of gradient color stops.
*Required*: No
*Type*: Array of [GradientStop](aws-properties-quicksight-analysis-gradientstop.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
