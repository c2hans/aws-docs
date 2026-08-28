---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-excludeperiodconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ExcludePeriodConfiguration
<a name="aws-properties-quicksight-analysis-excludeperiodconfiguration"></a>

The exclude period of `TimeRangeFilter` or `RelativeDatesFilter`.

## Syntax
<a name="aws-properties-quicksight-analysis-excludeperiodconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-excludeperiodconfiguration-syntax.json"></a>

```
{
  "[Amount](#cfn-quicksight-analysis-excludeperiodconfiguration-amount)" : {{Number}},
  "[Granularity](#cfn-quicksight-analysis-excludeperiodconfiguration-granularity)" : {{String}},
  "[Status](#cfn-quicksight-analysis-excludeperiodconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-excludeperiodconfiguration-syntax.yaml"></a>

```
  [Amount](#cfn-quicksight-analysis-excludeperiodconfiguration-amount): {{Number}}
  [Granularity](#cfn-quicksight-analysis-excludeperiodconfiguration-granularity): {{String}}
  [Status](#cfn-quicksight-analysis-excludeperiodconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-excludeperiodconfiguration-properties"></a>

`Amount`  <a name="cfn-quicksight-analysis-excludeperiodconfiguration-amount"></a>
The amount or number of the exclude period.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Granularity`  <a name="cfn-quicksight-analysis-excludeperiodconfiguration-granularity"></a>
The granularity or unit (day, month, year) of the exclude period.
*Required*: Yes
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-analysis-excludeperiodconfiguration-status"></a>
The status of the exclude period. Choose from the following options:
+  `ENABLED`
+  `DISABLED`
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
