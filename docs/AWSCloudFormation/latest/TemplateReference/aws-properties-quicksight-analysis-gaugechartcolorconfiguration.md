---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-gaugechartcolorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GaugeChartColorConfiguration
<a name="aws-properties-quicksight-analysis-gaugechartcolorconfiguration"></a>

The color configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-gaugechartcolorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-gaugechartcolorconfiguration-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-analysis-gaugechartcolorconfiguration-backgroundcolor)" : {{String}},
  "[ForegroundColor](#cfn-quicksight-analysis-gaugechartcolorconfiguration-foregroundcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-gaugechartcolorconfiguration-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-analysis-gaugechartcolorconfiguration-backgroundcolor): {{String}}
  [ForegroundColor](#cfn-quicksight-analysis-gaugechartcolorconfiguration-foregroundcolor): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-gaugechartcolorconfiguration-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-analysis-gaugechartcolorconfiguration-backgroundcolor"></a>
The background color configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForegroundColor`  <a name="cfn-quicksight-analysis-gaugechartcolorconfiguration-foregroundcolor"></a>
The foreground color configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
