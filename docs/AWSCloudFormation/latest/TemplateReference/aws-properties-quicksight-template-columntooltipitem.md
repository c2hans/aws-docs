---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-columntooltipitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ColumnTooltipItem
<a name="aws-properties-quicksight-template-columntooltipitem"></a>

The tooltip item for the columns that are not part of a field well.

## Syntax
<a name="aws-properties-quicksight-template-columntooltipitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-columntooltipitem-syntax.json"></a>

```
{
  "[Aggregation](#cfn-quicksight-template-columntooltipitem-aggregation)" : {{AggregationFunction}},
  "[Column](#cfn-quicksight-template-columntooltipitem-column)" : {{ColumnIdentifier}},
  "[Label](#cfn-quicksight-template-columntooltipitem-label)" : {{String}},
  "[TooltipTarget](#cfn-quicksight-template-columntooltipitem-tooltiptarget)" : {{String}},
  "[Visibility](#cfn-quicksight-template-columntooltipitem-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-columntooltipitem-syntax.yaml"></a>

```
  [Aggregation](#cfn-quicksight-template-columntooltipitem-aggregation): {{
    AggregationFunction}}
  [Column](#cfn-quicksight-template-columntooltipitem-column): {{
    ColumnIdentifier}}
  [Label](#cfn-quicksight-template-columntooltipitem-label): {{String}}
  [TooltipTarget](#cfn-quicksight-template-columntooltipitem-tooltiptarget): {{String}}
  [Visibility](#cfn-quicksight-template-columntooltipitem-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-columntooltipitem-properties"></a>

`Aggregation`  <a name="cfn-quicksight-template-columntooltipitem-aggregation"></a>
The aggregation function of the column tooltip item.
*Required*: No
*Type*: [AggregationFunction](aws-properties-quicksight-template-aggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Column`  <a name="cfn-quicksight-template-columntooltipitem-column"></a>
The target column of the tooltip item.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-template-columntooltipitem-label"></a>
The label of the tooltip item.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipTarget`  <a name="cfn-quicksight-template-columntooltipitem-tooltiptarget"></a>
Determines the target of the column tooltip item in a combo chart visual.
*Required*: No
*Type*: String
*Allowed values*: `BOTH | BAR | LINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-columntooltipitem-visibility"></a>
The visibility of the tooltip item.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
