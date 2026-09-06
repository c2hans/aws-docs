---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-arcoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ArcOptions
<a name="aws-properties-quicksight-dashboard-arcoptions"></a>

The options that determine the arc thickness of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-arcoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-arcoptions-syntax.json"></a>

```
{
  "[ArcThickness](#cfn-quicksight-dashboard-arcoptions-arcthickness)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-arcoptions-syntax.yaml"></a>

```
  [ArcThickness](#cfn-quicksight-dashboard-arcoptions-arcthickness): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-arcoptions-properties"></a>

`ArcThickness`  <a name="cfn-quicksight-dashboard-arcoptions-arcthickness"></a>
The arc thickness of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Allowed values*: `SMALL | MEDIUM | LARGE | WHOLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
