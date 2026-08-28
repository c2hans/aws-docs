---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-wordcloudaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template WordCloudAggregatedFieldWells
<a name="aws-properties-quicksight-template-wordcloudaggregatedfieldwells"></a>

The aggregated field wells of a word cloud.

## Syntax
<a name="aws-properties-quicksight-template-wordcloudaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-wordcloudaggregatedfieldwells-syntax.json"></a>

```
{
  "[GroupBy](#cfn-quicksight-template-wordcloudaggregatedfieldwells-groupby)" : {{[ DimensionField, ... ]}},
  "[Size](#cfn-quicksight-template-wordcloudaggregatedfieldwells-size)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-wordcloudaggregatedfieldwells-syntax.yaml"></a>

```
  [GroupBy](#cfn-quicksight-template-wordcloudaggregatedfieldwells-groupby): {{
    - DimensionField}}
  [Size](#cfn-quicksight-template-wordcloudaggregatedfieldwells-size): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-wordcloudaggregatedfieldwells-properties"></a>

`GroupBy`  <a name="cfn-quicksight-template-wordcloudaggregatedfieldwells-groupby"></a>
The group by field well of a word cloud. Values are grouped by group by fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-quicksight-template-wordcloudaggregatedfieldwells-size"></a>
The size field well of a word cloud. Values are aggregated based on group by fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
