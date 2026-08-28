---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-linechartmarkerstylesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LineChartMarkerStyleSettings
<a name="aws-properties-quicksight-analysis-linechartmarkerstylesettings"></a>

Marker styles options for a line series in `LineChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-linechartmarkerstylesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-linechartmarkerstylesettings-syntax.json"></a>

```
{
  "[MarkerColor](#cfn-quicksight-analysis-linechartmarkerstylesettings-markercolor)" : {{String}},
  "[MarkerShape](#cfn-quicksight-analysis-linechartmarkerstylesettings-markershape)" : {{String}},
  "[MarkerSize](#cfn-quicksight-analysis-linechartmarkerstylesettings-markersize)" : {{String}},
  "[MarkerVisibility](#cfn-quicksight-analysis-linechartmarkerstylesettings-markervisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-linechartmarkerstylesettings-syntax.yaml"></a>

```
  [MarkerColor](#cfn-quicksight-analysis-linechartmarkerstylesettings-markercolor): {{String}}
  [MarkerShape](#cfn-quicksight-analysis-linechartmarkerstylesettings-markershape): {{String}}
  [MarkerSize](#cfn-quicksight-analysis-linechartmarkerstylesettings-markersize): {{String}}
  [MarkerVisibility](#cfn-quicksight-analysis-linechartmarkerstylesettings-markervisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-linechartmarkerstylesettings-properties"></a>

`MarkerColor`  <a name="cfn-quicksight-analysis-linechartmarkerstylesettings-markercolor"></a>
Color of marker in the series.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerShape`  <a name="cfn-quicksight-analysis-linechartmarkerstylesettings-markershape"></a>
Shape option for markers in the series.
+ `CIRCLE`: Show marker as a circle.
+ `TRIANGLE`: Show marker as a triangle.
+ `SQUARE`: Show marker as a square.
+ `DIAMOND`: Show marker as a diamond.
+ `ROUNDED_SQUARE`: Show marker as a rounded square.
*Required*: No
*Type*: String
*Allowed values*: `CIRCLE | TRIANGLE | SQUARE | DIAMOND | ROUNDED_SQUARE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerSize`  <a name="cfn-quicksight-analysis-linechartmarkerstylesettings-markersize"></a>
Size of marker in the series.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerVisibility`  <a name="cfn-quicksight-analysis-linechartmarkerstylesettings-markervisibility"></a>
Configuration option that determines whether to show the markers in the series.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
