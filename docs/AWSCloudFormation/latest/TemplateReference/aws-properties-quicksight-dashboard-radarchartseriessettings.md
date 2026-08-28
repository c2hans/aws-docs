---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-radarchartseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard RadarChartSeriesSettings
<a name="aws-properties-quicksight-dashboard-radarchartseriessettings"></a>

The series settings of a radar chart.

## Syntax
<a name="aws-properties-quicksight-dashboard-radarchartseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-radarchartseriessettings-syntax.json"></a>

```
{
  "[AreaStyleSettings](#cfn-quicksight-dashboard-radarchartseriessettings-areastylesettings)" : {{RadarChartAreaStyleSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-radarchartseriessettings-syntax.yaml"></a>

```
  [AreaStyleSettings](#cfn-quicksight-dashboard-radarchartseriessettings-areastylesettings): {{
    RadarChartAreaStyleSettings}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-radarchartseriessettings-properties"></a>

`AreaStyleSettings`  <a name="cfn-quicksight-dashboard-radarchartseriessettings-areastylesettings"></a>
The area style settings of a radar chart.
*Required*: No
*Type*: [RadarChartAreaStyleSettings](aws-properties-quicksight-dashboard-radarchartareastylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
