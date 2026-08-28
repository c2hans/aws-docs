---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-fieldseriesitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FieldSeriesItem
<a name="aws-properties-quicksight-analysis-fieldseriesitem"></a>

The field series item configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-analysis-fieldseriesitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-fieldseriesitem-syntax.json"></a>

```
{
  "[AxisBinding](#cfn-quicksight-analysis-fieldseriesitem-axisbinding)" : {{String}},
  "[FieldId](#cfn-quicksight-analysis-fieldseriesitem-fieldid)" : {{String}},
  "[Settings](#cfn-quicksight-analysis-fieldseriesitem-settings)" : {{LineChartSeriesSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-fieldseriesitem-syntax.yaml"></a>

```
  [AxisBinding](#cfn-quicksight-analysis-fieldseriesitem-axisbinding): {{String}}
  [FieldId](#cfn-quicksight-analysis-fieldseriesitem-fieldid): {{String}}
  [Settings](#cfn-quicksight-analysis-fieldseriesitem-settings): {{
    LineChartSeriesSettings}}
```

## Properties
<a name="aws-properties-quicksight-analysis-fieldseriesitem-properties"></a>

`AxisBinding`  <a name="cfn-quicksight-analysis-fieldseriesitem-axisbinding"></a>
The axis that you are binding the field to.
*Required*: Yes
*Type*: String
*Allowed values*: `PRIMARY_YAXIS | SECONDARY_YAXIS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-analysis-fieldseriesitem-fieldid"></a>
The field ID of the field for which you are setting the axis binding.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-quicksight-analysis-fieldseriesitem-settings"></a>
The options that determine the presentation of line series associated to the field.
*Required*: No
*Type*: [LineChartSeriesSettings](aws-properties-quicksight-analysis-linechartseriessettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
