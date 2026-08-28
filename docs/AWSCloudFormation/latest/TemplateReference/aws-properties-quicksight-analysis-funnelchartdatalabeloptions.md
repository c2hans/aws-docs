---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-funnelchartdatalabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FunnelChartDataLabelOptions
<a name="aws-properties-quicksight-analysis-funnelchartdatalabeloptions"></a>

The options that determine the presentation of the data labels.

## Syntax
<a name="aws-properties-quicksight-analysis-funnelchartdatalabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-funnelchartdatalabeloptions-syntax.json"></a>

```
{
  "[CategoryLabelVisibility](#cfn-quicksight-analysis-funnelchartdatalabeloptions-categorylabelvisibility)" : {{String}},
  "[LabelColor](#cfn-quicksight-analysis-funnelchartdatalabeloptions-labelcolor)" : {{String}},
  "[LabelFontConfiguration](#cfn-quicksight-analysis-funnelchartdatalabeloptions-labelfontconfiguration)" : {{FontConfiguration}},
  "[MeasureDataLabelStyle](#cfn-quicksight-analysis-funnelchartdatalabeloptions-measuredatalabelstyle)" : {{String}},
  "[MeasureLabelVisibility](#cfn-quicksight-analysis-funnelchartdatalabeloptions-measurelabelvisibility)" : {{String}},
  "[Position](#cfn-quicksight-analysis-funnelchartdatalabeloptions-position)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-funnelchartdatalabeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-funnelchartdatalabeloptions-syntax.yaml"></a>

```
  [CategoryLabelVisibility](#cfn-quicksight-analysis-funnelchartdatalabeloptions-categorylabelvisibility): {{String}}
  [LabelColor](#cfn-quicksight-analysis-funnelchartdatalabeloptions-labelcolor): {{String}}
  [LabelFontConfiguration](#cfn-quicksight-analysis-funnelchartdatalabeloptions-labelfontconfiguration): {{
    FontConfiguration}}
  [MeasureDataLabelStyle](#cfn-quicksight-analysis-funnelchartdatalabeloptions-measuredatalabelstyle): {{String}}
  [MeasureLabelVisibility](#cfn-quicksight-analysis-funnelchartdatalabeloptions-measurelabelvisibility): {{String}}
  [Position](#cfn-quicksight-analysis-funnelchartdatalabeloptions-position): {{String}}
  [Visibility](#cfn-quicksight-analysis-funnelchartdatalabeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-funnelchartdatalabeloptions-properties"></a>

`CategoryLabelVisibility`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-categorylabelvisibility"></a>
The visibility of the category labels within the data labels.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelColor`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-labelcolor"></a>
The color of the data label text.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelFontConfiguration`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-labelfontconfiguration"></a>
The font configuration for the data labels.
Only the `FontSize` attribute of the font configuration is used for data labels.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-analysis-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MeasureDataLabelStyle`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-measuredatalabelstyle"></a>
Determines the style of the metric labels.
*Required*: No
*Type*: String
*Allowed values*: `VALUE_ONLY | PERCENTAGE_BY_FIRST_STAGE | PERCENTAGE_BY_PREVIOUS_STAGE | VALUE_AND_PERCENTAGE_BY_FIRST_STAGE | VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MeasureLabelVisibility`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-measurelabelvisibility"></a>
The visibility of the measure labels within the data labels.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Position`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-position"></a>
Determines the positioning of the data label relative to a section of the funnel.
*Required*: No
*Type*: String
*Allowed values*: `INSIDE | OUTSIDE | LEFT | TOP | BOTTOM | RIGHT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-funnelchartdatalabeloptions-visibility"></a>
The visibility option that determines if data labels are displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
