---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-histogramaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard HistogramAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-histogramaggregatedfieldwells"></a>

The field well configuration of a histogram.

## Syntax
<a name="aws-properties-quicksight-dashboard-histogramaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-histogramaggregatedfieldwells-syntax.json"></a>

```
{
  "[Values](#cfn-quicksight-dashboard-histogramaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-histogramaggregatedfieldwells-syntax.yaml"></a>

```
  [Values](#cfn-quicksight-dashboard-histogramaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-histogramaggregatedfieldwells-properties"></a>

`Values`  <a name="cfn-quicksight-dashboard-histogramaggregatedfieldwells-values"></a>
The value field wells of a histogram. Values are aggregated by `COUNT` or `DISTINCT_COUNT`.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
