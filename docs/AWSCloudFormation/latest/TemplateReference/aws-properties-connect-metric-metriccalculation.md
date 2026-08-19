---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-metriccalculation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric MetricCalculation
<a name="aws-properties-connect-metric-metriccalculation"></a>

Contains the formula and component metrics that define a custom metric calculation.

## Syntax
<a name="aws-properties-connect-metric-metriccalculation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-metriccalculation-syntax.json"></a>

```
{
  "[Calculation](#cfn-connect-metric-metriccalculation-calculation)" : {{String}},
  "[CalculationComponents](#cfn-connect-metric-metriccalculation-calculationcomponents)" : {{[ CalculationComponent, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-metric-metriccalculation-syntax.yaml"></a>

```
  [Calculation](#cfn-connect-metric-metriccalculation-calculation): {{String}}
  [CalculationComponents](#cfn-connect-metric-metriccalculation-calculationcomponents): {{
    - CalculationComponent}}
```

## Properties
<a name="aws-properties-connect-metric-metriccalculation-properties"></a>

`Calculation`  <a name="cfn-connect-metric-metriccalculation-calculation"></a>
The formula expression that defines how the metric is calculated. Uses component aliases (for example, `100 * SUM(M1) / SUM(M2)`).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CalculationComponents`  <a name="cfn-connect-metric-metriccalculation-calculationcomponents"></a>
The list of component metrics referenced in the calculation formula. Each component has an alias used in the formula expression.
*Required*: Yes
*Type*: Array of [CalculationComponent](aws-properties-connect-metric-calculationcomponent.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
