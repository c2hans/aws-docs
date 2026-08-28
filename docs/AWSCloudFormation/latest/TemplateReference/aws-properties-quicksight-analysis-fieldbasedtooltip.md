---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-fieldbasedtooltip.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FieldBasedTooltip
<a name="aws-properties-quicksight-analysis-fieldbasedtooltip"></a>

The setup for the detailed tooltip.

## Syntax
<a name="aws-properties-quicksight-analysis-fieldbasedtooltip-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-fieldbasedtooltip-syntax.json"></a>

```
{
  "[AggregationVisibility](#cfn-quicksight-analysis-fieldbasedtooltip-aggregationvisibility)" : {{String}},
  "[TooltipFields](#cfn-quicksight-analysis-fieldbasedtooltip-tooltipfields)" : {{[ TooltipItem, ... ]}},
  "[TooltipTitleType](#cfn-quicksight-analysis-fieldbasedtooltip-tooltiptitletype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-fieldbasedtooltip-syntax.yaml"></a>

```
  [AggregationVisibility](#cfn-quicksight-analysis-fieldbasedtooltip-aggregationvisibility): {{String}}
  [TooltipFields](#cfn-quicksight-analysis-fieldbasedtooltip-tooltipfields): {{
    - TooltipItem}}
  [TooltipTitleType](#cfn-quicksight-analysis-fieldbasedtooltip-tooltiptitletype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-fieldbasedtooltip-properties"></a>

`AggregationVisibility`  <a name="cfn-quicksight-analysis-fieldbasedtooltip-aggregationvisibility"></a>
The visibility of `Show aggregations`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipFields`  <a name="cfn-quicksight-analysis-fieldbasedtooltip-tooltipfields"></a>
The fields configuration in the tooltip.
*Required*: No
*Type*: Array of [TooltipItem](aws-properties-quicksight-analysis-tooltipitem.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipTitleType`  <a name="cfn-quicksight-analysis-fieldbasedtooltip-tooltiptitletype"></a>
The type for the >tooltip title. Choose one of the following options:
+ `NONE`: Doesn't use the primary value as the title.
+ `PRIMARY_VALUE`: Uses primary value as the title.
*Required*: No
*Type*: String
*Allowed values*: `NONE | PRIMARY_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
