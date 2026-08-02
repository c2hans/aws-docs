---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-treemapaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TreeMapAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-treemapaggregatedfieldwells"></a>

Aggregated field wells of a tree map.

## Syntax
<a name="aws-properties-quicksight-analysis-treemapaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-treemapaggregatedfieldwells-syntax.json"></a>

```
{
  "[Colors](#cfn-quicksight-analysis-treemapaggregatedfieldwells-colors)" : {{[ MeasureField, ... ]}},
  "[Groups](#cfn-quicksight-analysis-treemapaggregatedfieldwells-groups)" : {{[ DimensionField, ... ]}},
  "[Sizes](#cfn-quicksight-analysis-treemapaggregatedfieldwells-sizes)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-treemapaggregatedfieldwells-syntax.yaml"></a>

```
  [Colors](#cfn-quicksight-analysis-treemapaggregatedfieldwells-colors): {{
    - MeasureField}}
  [Groups](#cfn-quicksight-analysis-treemapaggregatedfieldwells-groups): {{
    - DimensionField}}
  [Sizes](#cfn-quicksight-analysis-treemapaggregatedfieldwells-sizes): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-treemapaggregatedfieldwells-properties"></a>

`Colors`  <a name="cfn-quicksight-analysis-treemapaggregatedfieldwells-colors"></a>
The color field well of a tree map. Values are grouped by aggregations based on group by fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Groups`  <a name="cfn-quicksight-analysis-treemapaggregatedfieldwells-groups"></a>
The group by field well of a tree map. Values are grouped based on group by fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sizes`  <a name="cfn-quicksight-analysis-treemapaggregatedfieldwells-sizes"></a>
The size field well of a tree map. Values are aggregated based on group by fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
