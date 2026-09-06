---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-combochartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ComboChartAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-combochartaggregatedfieldwells"></a>

The aggregated field wells of a combo chart.

## Syntax
<a name="aws-properties-quicksight-analysis-combochartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-combochartaggregatedfieldwells-syntax.json"></a>

```
{
  "[BarValues](#cfn-quicksight-analysis-combochartaggregatedfieldwells-barvalues)" : {{[ MeasureField, ... ]}},
  "[Category](#cfn-quicksight-analysis-combochartaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Colors](#cfn-quicksight-analysis-combochartaggregatedfieldwells-colors)" : {{[ DimensionField, ... ]}},
  "[LineValues](#cfn-quicksight-analysis-combochartaggregatedfieldwells-linevalues)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-combochartaggregatedfieldwells-syntax.yaml"></a>

```
  [BarValues](#cfn-quicksight-analysis-combochartaggregatedfieldwells-barvalues): {{
    - MeasureField}}
  [Category](#cfn-quicksight-analysis-combochartaggregatedfieldwells-category): {{
    - DimensionField}}
  [Colors](#cfn-quicksight-analysis-combochartaggregatedfieldwells-colors): {{
    - DimensionField}}
  [LineValues](#cfn-quicksight-analysis-combochartaggregatedfieldwells-linevalues): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-combochartaggregatedfieldwells-properties"></a>

`BarValues`  <a name="cfn-quicksight-analysis-combochartaggregatedfieldwells-barvalues"></a>
The aggregated `BarValues` field well of a combo chart.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Category`  <a name="cfn-quicksight-analysis-combochartaggregatedfieldwells-category"></a>
The aggregated category field wells of a combo chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Colors`  <a name="cfn-quicksight-analysis-combochartaggregatedfieldwells-colors"></a>
The aggregated colors field well of a combo chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineValues`  <a name="cfn-quicksight-analysis-combochartaggregatedfieldwells-linevalues"></a>
The aggregated `LineValues` field well of a combo chart.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
