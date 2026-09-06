---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-gaugechartfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GaugeChartFieldWells
<a name="aws-properties-quicksight-template-gaugechartfieldwells"></a>

The field well configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-gaugechartfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-gaugechartfieldwells-syntax.json"></a>

```
{
  "[TargetValues](#cfn-quicksight-template-gaugechartfieldwells-targetvalues)" : {{[ MeasureField, ... ]}},
  "[Values](#cfn-quicksight-template-gaugechartfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-gaugechartfieldwells-syntax.yaml"></a>

```
  [TargetValues](#cfn-quicksight-template-gaugechartfieldwells-targetvalues): {{
    - MeasureField}}
  [Values](#cfn-quicksight-template-gaugechartfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-gaugechartfieldwells-properties"></a>

`TargetValues`  <a name="cfn-quicksight-template-gaugechartfieldwells-targetvalues"></a>
The target value field wells of a `GaugeChartVisual`.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-gaugechartfieldwells-values"></a>
The value field wells of a `GaugeChartVisual`.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
