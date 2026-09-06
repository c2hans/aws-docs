---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-scatterplotunaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ScatterPlotUnaggregatedFieldWells
<a name="aws-properties-quicksight-template-scatterplotunaggregatedfieldwells"></a>

The unaggregated field wells of a scatter plot.

## Syntax
<a name="aws-properties-quicksight-template-scatterplotunaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-scatterplotunaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Label](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-label)" : {{[ DimensionField, ... ]}},
  "[Size](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-size)" : {{[ MeasureField, ... ]}},
  "[XAxis](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-xaxis)" : {{[ DimensionField, ... ]}},
  "[YAxis](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-yaxis)" : {{[ DimensionField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-scatterplotunaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-category): {{
    - DimensionField}}
  [Label](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-label): {{
    - DimensionField}}
  [Size](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-size): {{
    - MeasureField}}
  [XAxis](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-xaxis): {{
    - DimensionField}}
  [YAxis](#cfn-quicksight-template-scatterplotunaggregatedfieldwells-yaxis): {{
    - DimensionField}}
```

## Properties
<a name="aws-properties-quicksight-template-scatterplotunaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-template-scatterplotunaggregatedfieldwells-category"></a>
The category field well of a scatter plot.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-template-scatterplotunaggregatedfieldwells-label"></a>
The label field well of a scatter plot.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-quicksight-template-scatterplotunaggregatedfieldwells-size"></a>
The size field well of a scatter plot.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxis`  <a name="cfn-quicksight-template-scatterplotunaggregatedfieldwells-xaxis"></a>
The x-axis field well of a scatter plot.
The x-axis is a dimension field and cannot be aggregated.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxis`  <a name="cfn-quicksight-template-scatterplotunaggregatedfieldwells-yaxis"></a>
The y-axis field well of a scatter plot.
The y-axis is a dimension field and cannot be aggregated.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
