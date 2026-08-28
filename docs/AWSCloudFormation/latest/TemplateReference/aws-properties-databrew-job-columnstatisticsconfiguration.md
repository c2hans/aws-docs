---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-columnstatisticsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job ColumnStatisticsConfiguration
<a name="aws-properties-databrew-job-columnstatisticsconfiguration"></a>

Configuration for column evaluations for a profile job. ColumnStatisticsConfiguration can be used to select evaluations and override parameters of evaluations for particular columns.

## Syntax
<a name="aws-properties-databrew-job-columnstatisticsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-columnstatisticsconfiguration-syntax.json"></a>

```
{
  "[Selectors](#cfn-databrew-job-columnstatisticsconfiguration-selectors)" : {{[ ColumnSelector, ... ]}},
  "[Statistics](#cfn-databrew-job-columnstatisticsconfiguration-statistics)" : {{StatisticsConfiguration}}
}
```

### YAML
<a name="aws-properties-databrew-job-columnstatisticsconfiguration-syntax.yaml"></a>

```
  [Selectors](#cfn-databrew-job-columnstatisticsconfiguration-selectors): {{
    - ColumnSelector}}
  [Statistics](#cfn-databrew-job-columnstatisticsconfiguration-statistics): {{
    StatisticsConfiguration}}
```

## Properties
<a name="aws-properties-databrew-job-columnstatisticsconfiguration-properties"></a>

`Selectors`  <a name="cfn-databrew-job-columnstatisticsconfiguration-selectors"></a>
List of column selectors. Selectors can be used to select columns from the dataset. When selectors are undefined, configuration will be applied to all supported columns.
*Required*: No
*Type*: Array of [ColumnSelector](aws-properties-databrew-job-columnselector.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Statistics`  <a name="cfn-databrew-job-columnstatisticsconfiguration-statistics"></a>
Configuration for evaluations. Statistics can be used to select evaluations and override parameters of evaluations.
*Required*: Yes
*Type*: [StatisticsConfiguration](aws-properties-databrew-job-statisticsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
