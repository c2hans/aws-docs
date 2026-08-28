---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-subtotaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SubtotalOptions
<a name="aws-properties-quicksight-dashboard-subtotaloptions"></a>

The subtotal options.

## Syntax
<a name="aws-properties-quicksight-dashboard-subtotaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-subtotaloptions-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-dashboard-subtotaloptions-customlabel)" : {{String}},
  "[FieldLevel](#cfn-quicksight-dashboard-subtotaloptions-fieldlevel)" : {{String}},
  "[FieldLevelOptions](#cfn-quicksight-dashboard-subtotaloptions-fieldleveloptions)" : {{[ PivotTableFieldSubtotalOptions, ... ]}},
  "[MetricHeaderCellStyle](#cfn-quicksight-dashboard-subtotaloptions-metricheadercellstyle)" : {{TableCellStyle}},
  "[StyleTargets](#cfn-quicksight-dashboard-subtotaloptions-styletargets)" : {{[ TableStyleTarget, ... ]}},
  "[TotalCellStyle](#cfn-quicksight-dashboard-subtotaloptions-totalcellstyle)" : {{TableCellStyle}},
  "[TotalsVisibility](#cfn-quicksight-dashboard-subtotaloptions-totalsvisibility)" : {{String}},
  "[ValueCellStyle](#cfn-quicksight-dashboard-subtotaloptions-valuecellstyle)" : {{TableCellStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-subtotaloptions-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-dashboard-subtotaloptions-customlabel): {{String}}
  [FieldLevel](#cfn-quicksight-dashboard-subtotaloptions-fieldlevel): {{String}}
  [FieldLevelOptions](#cfn-quicksight-dashboard-subtotaloptions-fieldleveloptions): {{
    - PivotTableFieldSubtotalOptions}}
  [MetricHeaderCellStyle](#cfn-quicksight-dashboard-subtotaloptions-metricheadercellstyle): {{
    TableCellStyle}}
  [StyleTargets](#cfn-quicksight-dashboard-subtotaloptions-styletargets): {{
    - TableStyleTarget}}
  [TotalCellStyle](#cfn-quicksight-dashboard-subtotaloptions-totalcellstyle): {{
    TableCellStyle}}
  [TotalsVisibility](#cfn-quicksight-dashboard-subtotaloptions-totalsvisibility): {{String}}
  [ValueCellStyle](#cfn-quicksight-dashboard-subtotaloptions-valuecellstyle): {{
    TableCellStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-subtotaloptions-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-dashboard-subtotaloptions-customlabel"></a>
The custom label string for the subtotal cells.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldLevel`  <a name="cfn-quicksight-dashboard-subtotaloptions-fieldlevel"></a>
The field level (all, custom, last) for the subtotal cells.
*Required*: No
*Type*: String
*Allowed values*: `ALL | CUSTOM | LAST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldLevelOptions`  <a name="cfn-quicksight-dashboard-subtotaloptions-fieldleveloptions"></a>
The optional configuration of subtotal cells.
*Required*: No
*Type*: Array of [PivotTableFieldSubtotalOptions](aws-properties-quicksight-dashboard-pivottablefieldsubtotaloptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricHeaderCellStyle`  <a name="cfn-quicksight-dashboard-subtotaloptions-metricheadercellstyle"></a>
The cell styling options for the subtotals of header cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-dashboard-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleTargets`  <a name="cfn-quicksight-dashboard-subtotaloptions-styletargets"></a>
The style targets options for subtotals.
*Required*: No
*Type*: Array of [TableStyleTarget](aws-properties-quicksight-dashboard-tablestyletarget.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalCellStyle`  <a name="cfn-quicksight-dashboard-subtotaloptions-totalcellstyle"></a>
The cell styling options for the subtotal cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-dashboard-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalsVisibility`  <a name="cfn-quicksight-dashboard-subtotaloptions-totalsvisibility"></a>
The visibility configuration for the subtotal cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueCellStyle`  <a name="cfn-quicksight-dashboard-subtotaloptions-valuecellstyle"></a>
The cell styling options for the subtotals of value cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-dashboard-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
