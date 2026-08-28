---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-forecastconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ForecastConfiguration
<a name="aws-properties-quicksight-analysis-forecastconfiguration"></a>

The forecast configuration that is used in a line chart's display properties.

## Syntax
<a name="aws-properties-quicksight-analysis-forecastconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-forecastconfiguration-syntax.json"></a>

```
{
  "[ForecastProperties](#cfn-quicksight-analysis-forecastconfiguration-forecastproperties)" : {{TimeBasedForecastProperties}},
  "[Scenario](#cfn-quicksight-analysis-forecastconfiguration-scenario)" : {{ForecastScenario}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-forecastconfiguration-syntax.yaml"></a>

```
  [ForecastProperties](#cfn-quicksight-analysis-forecastconfiguration-forecastproperties): {{
    TimeBasedForecastProperties}}
  [Scenario](#cfn-quicksight-analysis-forecastconfiguration-scenario): {{
    ForecastScenario}}
```

## Properties
<a name="aws-properties-quicksight-analysis-forecastconfiguration-properties"></a>

`ForecastProperties`  <a name="cfn-quicksight-analysis-forecastconfiguration-forecastproperties"></a>
The forecast properties setup of a forecast in the line chart.
*Required*: No
*Type*: [TimeBasedForecastProperties](aws-properties-quicksight-analysis-timebasedforecastproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scenario`  <a name="cfn-quicksight-analysis-forecastconfiguration-scenario"></a>
The forecast scenario of a forecast in the line chart.
*Required*: No
*Type*: [ForecastScenario](aws-properties-quicksight-analysis-forecastscenario.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
