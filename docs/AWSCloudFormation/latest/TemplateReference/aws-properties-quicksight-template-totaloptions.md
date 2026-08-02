---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-totaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TotalOptions
<a name="aws-properties-quicksight-template-totaloptions"></a>

The total options for a table visual.

## Syntax
<a name="aws-properties-quicksight-template-totaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-totaloptions-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-template-totaloptions-customlabel)" : {{String}},
  "[Placement](#cfn-quicksight-template-totaloptions-placement)" : {{String}},
  "[ScrollStatus](#cfn-quicksight-template-totaloptions-scrollstatus)" : {{String}},
  "[TotalAggregationOptions](#cfn-quicksight-template-totaloptions-totalaggregationoptions)" : {{[ TotalAggregationOption, ... ]}},
  "[TotalCellStyle](#cfn-quicksight-template-totaloptions-totalcellstyle)" : {{TableCellStyle}},
  "[TotalsVisibility](#cfn-quicksight-template-totaloptions-totalsvisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-totaloptions-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-template-totaloptions-customlabel): {{String}}
  [Placement](#cfn-quicksight-template-totaloptions-placement): {{String}}
  [ScrollStatus](#cfn-quicksight-template-totaloptions-scrollstatus): {{String}}
  [TotalAggregationOptions](#cfn-quicksight-template-totaloptions-totalaggregationoptions): {{
    - TotalAggregationOption}}
  [TotalCellStyle](#cfn-quicksight-template-totaloptions-totalcellstyle): {{
    TableCellStyle}}
  [TotalsVisibility](#cfn-quicksight-template-totaloptions-totalsvisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-totaloptions-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-template-totaloptions-customlabel"></a>
The custom label string for the total cells.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placement`  <a name="cfn-quicksight-template-totaloptions-placement"></a>
The placement (start, end) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `START | END | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScrollStatus`  <a name="cfn-quicksight-template-totaloptions-scrollstatus"></a>
The scroll status (pinned, scrolled) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `PINNED | SCROLLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAggregationOptions`  <a name="cfn-quicksight-template-totaloptions-totalaggregationoptions"></a>
The total aggregation settings for each value field.
*Required*: No
*Type*: Array of [TotalAggregationOption](aws-properties-quicksight-template-totalaggregationoption.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalCellStyle`  <a name="cfn-quicksight-template-totaloptions-totalcellstyle"></a>
Cell styling options for the total cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-template-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalsVisibility`  <a name="cfn-quicksight-template-totaloptions-totalsvisibility"></a>
The visibility configuration for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
