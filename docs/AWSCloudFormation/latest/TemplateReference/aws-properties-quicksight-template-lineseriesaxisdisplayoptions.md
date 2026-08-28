---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-lineseriesaxisdisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template LineSeriesAxisDisplayOptions
<a name="aws-properties-quicksight-template-lineseriesaxisdisplayoptions"></a>

The series axis configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-template-lineseriesaxisdisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-lineseriesaxisdisplayoptions-syntax.json"></a>

```
{
  "[AxisOptions](#cfn-quicksight-template-lineseriesaxisdisplayoptions-axisoptions)" : {{AxisDisplayOptions}},
  "[MissingDataConfigurations](#cfn-quicksight-template-lineseriesaxisdisplayoptions-missingdataconfigurations)" : {{[ MissingDataConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-lineseriesaxisdisplayoptions-syntax.yaml"></a>

```
  [AxisOptions](#cfn-quicksight-template-lineseriesaxisdisplayoptions-axisoptions): {{
    AxisDisplayOptions}}
  [MissingDataConfigurations](#cfn-quicksight-template-lineseriesaxisdisplayoptions-missingdataconfigurations): {{
    - MissingDataConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-lineseriesaxisdisplayoptions-properties"></a>

`AxisOptions`  <a name="cfn-quicksight-template-lineseriesaxisdisplayoptions-axisoptions"></a>
The options that determine the presentation of the line series axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-template-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MissingDataConfigurations`  <a name="cfn-quicksight-template-lineseriesaxisdisplayoptions-missingdataconfigurations"></a>
The configuration options that determine how missing data is treated during the rendering of a line chart.
*Required*: No
*Type*: Array of [MissingDataConfiguration](aws-properties-quicksight-template-missingdataconfiguration.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
