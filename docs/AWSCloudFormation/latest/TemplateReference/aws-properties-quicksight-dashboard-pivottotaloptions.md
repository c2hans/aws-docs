---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-pivottotaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard PivotTotalOptions
<a name="aws-properties-quicksight-dashboard-pivottotaloptions"></a>

The optional configuration of totals cells in a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-pivottotaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-pivottotaloptions-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-dashboard-pivottotaloptions-customlabel)" : {{String}},
  "[MetricHeaderCellStyle](#cfn-quicksight-dashboard-pivottotaloptions-metricheadercellstyle)" : {{TableCellStyle}},
  "[Placement](#cfn-quicksight-dashboard-pivottotaloptions-placement)" : {{String}},
  "[ScrollStatus](#cfn-quicksight-dashboard-pivottotaloptions-scrollstatus)" : {{String}},
  "[TotalAggregationOptions](#cfn-quicksight-dashboard-pivottotaloptions-totalaggregationoptions)" : {{[ TotalAggregationOption, ... ]}},
  "[TotalCellStyle](#cfn-quicksight-dashboard-pivottotaloptions-totalcellstyle)" : {{TableCellStyle}},
  "[TotalsVisibility](#cfn-quicksight-dashboard-pivottotaloptions-totalsvisibility)" : {{String}},
  "[ValueCellStyle](#cfn-quicksight-dashboard-pivottotaloptions-valuecellstyle)" : {{TableCellStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-pivottotaloptions-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-dashboard-pivottotaloptions-customlabel): {{String}}
  [MetricHeaderCellStyle](#cfn-quicksight-dashboard-pivottotaloptions-metricheadercellstyle): {{
    TableCellStyle}}
  [Placement](#cfn-quicksight-dashboard-pivottotaloptions-placement): {{String}}
  [ScrollStatus](#cfn-quicksight-dashboard-pivottotaloptions-scrollstatus): {{String}}
  [TotalAggregationOptions](#cfn-quicksight-dashboard-pivottotaloptions-totalaggregationoptions): {{
    - TotalAggregationOption}}
  [TotalCellStyle](#cfn-quicksight-dashboard-pivottotaloptions-totalcellstyle): {{
    TableCellStyle}}
  [TotalsVisibility](#cfn-quicksight-dashboard-pivottotaloptions-totalsvisibility): {{String}}
  [ValueCellStyle](#cfn-quicksight-dashboard-pivottotaloptions-valuecellstyle): {{
    TableCellStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-pivottotaloptions-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-dashboard-pivottotaloptions-customlabel"></a>
The custom label string for the total cells.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricHeaderCellStyle`  <a name="cfn-quicksight-dashboard-pivottotaloptions-metricheadercellstyle"></a>
The cell styling options for the total of header cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-dashboard-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placement`  <a name="cfn-quicksight-dashboard-pivottotaloptions-placement"></a>
The placement (start, end) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `START | END | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScrollStatus`  <a name="cfn-quicksight-dashboard-pivottotaloptions-scrollstatus"></a>
The scroll status (pinned, scrolled) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `PINNED | SCROLLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAggregationOptions`  <a name="cfn-quicksight-dashboard-pivottotaloptions-totalaggregationoptions"></a>
The total aggregation options for each value field.
*Required*: No
*Type*: Array of [TotalAggregationOption](aws-properties-quicksight-dashboard-totalaggregationoption.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalCellStyle`  <a name="cfn-quicksight-dashboard-pivottotaloptions-totalcellstyle"></a>
The cell styling options for the total cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-dashboard-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalsVisibility`  <a name="cfn-quicksight-dashboard-pivottotaloptions-totalsvisibility"></a>
The visibility configuration for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueCellStyle`  <a name="cfn-quicksight-dashboard-pivottotaloptions-valuecellstyle"></a>
The cell styling options for the totals of value cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-dashboard-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
