---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialgradientcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialGradientColor
<a name="aws-properties-quicksight-analysis-geospatialgradientcolor"></a>

The definition for a gradient color.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialgradientcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialgradientcolor-syntax.json"></a>

```
{
  "[DefaultOpacity](#cfn-quicksight-analysis-geospatialgradientcolor-defaultopacity)" : {{Number}},
  "[NullDataSettings](#cfn-quicksight-analysis-geospatialgradientcolor-nulldatasettings)" : {{GeospatialNullDataSettings}},
  "[NullDataVisibility](#cfn-quicksight-analysis-geospatialgradientcolor-nulldatavisibility)" : {{String}},
  "[StepColors](#cfn-quicksight-analysis-geospatialgradientcolor-stepcolors)" : {{[ GeospatialGradientStepColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialgradientcolor-syntax.yaml"></a>

```
  [DefaultOpacity](#cfn-quicksight-analysis-geospatialgradientcolor-defaultopacity): {{Number}}
  [NullDataSettings](#cfn-quicksight-analysis-geospatialgradientcolor-nulldatasettings): {{
    GeospatialNullDataSettings}}
  [NullDataVisibility](#cfn-quicksight-analysis-geospatialgradientcolor-nulldatavisibility): {{String}}
  [StepColors](#cfn-quicksight-analysis-geospatialgradientcolor-stepcolors): {{
    - GeospatialGradientStepColor}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialgradientcolor-properties"></a>

`DefaultOpacity`  <a name="cfn-quicksight-analysis-geospatialgradientcolor-defaultopacity"></a>
The default opacity for the gradient color.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataSettings`  <a name="cfn-quicksight-analysis-geospatialgradientcolor-nulldatasettings"></a>
The null data visualization settings.
*Required*: No
*Type*: [GeospatialNullDataSettings](aws-properties-quicksight-analysis-geospatialnulldatasettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataVisibility`  <a name="cfn-quicksight-analysis-geospatialgradientcolor-nulldatavisibility"></a>
The state of visibility for null data.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepColors`  <a name="cfn-quicksight-analysis-geospatialgradientcolor-stepcolors"></a>
A list of gradient step colors for the gradient.
*Required*: Yes
*Type*: Array of [GeospatialGradientStepColor](aws-properties-quicksight-analysis-geospatialgradientstepcolor.md)
*Minimum*: `2`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
