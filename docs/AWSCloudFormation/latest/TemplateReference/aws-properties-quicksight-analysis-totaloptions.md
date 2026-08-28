---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-totaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TotalOptions
<a name="aws-properties-quicksight-analysis-totaloptions"></a>

The total options for a table visual.

## Syntax
<a name="aws-properties-quicksight-analysis-totaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-totaloptions-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-analysis-totaloptions-customlabel)" : {{String}},
  "[Placement](#cfn-quicksight-analysis-totaloptions-placement)" : {{String}},
  "[ScrollStatus](#cfn-quicksight-analysis-totaloptions-scrollstatus)" : {{String}},
  "[TotalAggregationOptions](#cfn-quicksight-analysis-totaloptions-totalaggregationoptions)" : {{[ TotalAggregationOption, ... ]}},
  "[TotalCellStyle](#cfn-quicksight-analysis-totaloptions-totalcellstyle)" : {{TableCellStyle}},
  "[TotalsVisibility](#cfn-quicksight-analysis-totaloptions-totalsvisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-totaloptions-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-analysis-totaloptions-customlabel): {{String}}
  [Placement](#cfn-quicksight-analysis-totaloptions-placement): {{String}}
  [ScrollStatus](#cfn-quicksight-analysis-totaloptions-scrollstatus): {{String}}
  [TotalAggregationOptions](#cfn-quicksight-analysis-totaloptions-totalaggregationoptions): {{
    - TotalAggregationOption}}
  [TotalCellStyle](#cfn-quicksight-analysis-totaloptions-totalcellstyle): {{
    TableCellStyle}}
  [TotalsVisibility](#cfn-quicksight-analysis-totaloptions-totalsvisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-totaloptions-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-analysis-totaloptions-customlabel"></a>
The custom label string for the total cells.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placement`  <a name="cfn-quicksight-analysis-totaloptions-placement"></a>
The placement (start, end) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `START | END | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScrollStatus`  <a name="cfn-quicksight-analysis-totaloptions-scrollstatus"></a>
The scroll status (pinned, scrolled) for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `PINNED | SCROLLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAggregationOptions`  <a name="cfn-quicksight-analysis-totaloptions-totalaggregationoptions"></a>
The total aggregation settings for each value field.
*Required*: No
*Type*: Array of [TotalAggregationOption](aws-properties-quicksight-analysis-totalaggregationoption.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalCellStyle`  <a name="cfn-quicksight-analysis-totaloptions-totalcellstyle"></a>
Cell styling options for the total cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-analysis-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalsVisibility`  <a name="cfn-quicksight-analysis-totaloptions-totalsvisibility"></a>
The visibility configuration for the total cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
