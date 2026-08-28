---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-timerangedrilldownfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TimeRangeDrillDownFilter
<a name="aws-properties-quicksight-dashboard-timerangedrilldownfilter"></a>

The time range drill down filter.

## Syntax
<a name="aws-properties-quicksight-dashboard-timerangedrilldownfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-timerangedrilldownfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-dashboard-timerangedrilldownfilter-column)" : {{ColumnIdentifier}},
  "[RangeMaximum](#cfn-quicksight-dashboard-timerangedrilldownfilter-rangemaximum)" : {{String}},
  "[RangeMinimum](#cfn-quicksight-dashboard-timerangedrilldownfilter-rangeminimum)" : {{String}},
  "[TimeGranularity](#cfn-quicksight-dashboard-timerangedrilldownfilter-timegranularity)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-timerangedrilldownfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-dashboard-timerangedrilldownfilter-column): {{
    ColumnIdentifier}}
  [RangeMaximum](#cfn-quicksight-dashboard-timerangedrilldownfilter-rangemaximum): {{String}}
  [RangeMinimum](#cfn-quicksight-dashboard-timerangedrilldownfilter-rangeminimum): {{String}}
  [TimeGranularity](#cfn-quicksight-dashboard-timerangedrilldownfilter-timegranularity): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-timerangedrilldownfilter-properties"></a>

`Column`  <a name="cfn-quicksight-dashboard-timerangedrilldownfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeMaximum`  <a name="cfn-quicksight-dashboard-timerangedrilldownfilter-rangemaximum"></a>
The maximum value for the filter value range.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeMinimum`  <a name="cfn-quicksight-dashboard-timerangedrilldownfilter-rangeminimum"></a>
The minimum value for the filter value range.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-dashboard-timerangedrilldownfilter-timegranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: Yes
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
