---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottotaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTotalOptions
<a name="aws-properties-quicksight-template-pivottotaloptions"></a>

The optional configuration of totals cells in a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-template-pivottotaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottotaloptions-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-template-pivottotaloptions-customlabel)" : {{String}},
  "[MetricHeaderCellStyle](#cfn-quicksight-template-pivottotaloptions-metricheadercellstyle)" : {{TableCellStyle}},
  "[Placement](#cfn-quicksight-template-pivottotaloptions-placement)" : {{String}},
  "[ScrollStatus](#cfn-quicksight-template-pivottotaloptions-scrollstatus)" : {{String}},
  "[TotalAggregationOptions](#cfn-quicksight-template-pivottotaloptions-totalaggregationoptions)" : {{[ TotalAggregationOption, ... ]}},
  "[TotalCellStyle](#cfn-quicksight-template-pivottotaloptions-totalcellstyle)" : {{TableCellStyle}},
  "[TotalsVisibility](#cfn-quicksight-template-pivottotaloptions-totalsvisibility)" : {{String}},
  "[ValueCellStyle](#cfn-quicksight-template-pivottotaloptions-valuecellstyle)" : {{TableCellStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottotaloptions-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-template-pivottotaloptions-customlabel): {{String}}
  [MetricHeaderCellStyle](#cfn-quicksight-template-pivottotaloptions-metricheadercellstyle): {{
    TableCellStyle}}
  [Placement](#cfn-quicksight-template-pivottotaloptions-placement): {{String}}
  [ScrollStatus](#cfn-quicksight-template-pivottotaloptions-scrollstatus): {{String}}
  [TotalAggregationOptions](#cfn-quicksight-template-pivottotaloptions-totalaggregationoptions): {{
    - TotalAggregationOption}}
  [TotalCellStyle](#cfn-quicksight-template-pivottotaloptions-totalcellstyle): {{
    TableCellStyle}}
  [TotalsVisibility](#cfn-quicksight-template-pivottotaloptions-totalsvisibility): {{String}}
  [ValueCellStyle](#cfn-quicksight-template-pivottotaloptions-valuecellstyle): {{
    TableCellStyle}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottotaloptions-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-template-pivottotaloptions-customlabel"></a>
The custom label string for the total cells.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricHeaderCellStyle`  <a name="cfn-quicksight-template-pivottotaloptions-metricheadercellstyle"></a>
The cell styling options for the total of header cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-template-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placement`  <a name="cfn-quicksight-template-pivottotaloptions-placement"></a>
The placement (start, end) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `START | END | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScrollStatus`  <a name="cfn-quicksight-template-pivottotaloptions-scrollstatus"></a>
The scroll status (pinned, scrolled) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `PINNED | SCROLLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAggregationOptions`  <a name="cfn-quicksight-template-pivottotaloptions-totalaggregationoptions"></a>
The total aggregation options for each value field.
*Required*: No
*Type*: Array of [TotalAggregationOption](aws-properties-quicksight-template-totalaggregationoption.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalCellStyle`  <a name="cfn-quicksight-template-pivottotaloptions-totalcellstyle"></a>
The cell styling options for the total cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-template-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalsVisibility`  <a name="cfn-quicksight-template-pivottotaloptions-totalsvisibility"></a>
The visibility configuration for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueCellStyle`  <a name="cfn-quicksight-template-pivottotaloptions-valuecellstyle"></a>
The cell styling options for the totals of value cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-template-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
