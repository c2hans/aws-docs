---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-arcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ArcConfiguration
<a name="aws-properties-quicksight-dashboard-arcconfiguration"></a>

The arc configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-arcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-arcconfiguration-syntax.json"></a>

```
{
  "[ArcAngle](#cfn-quicksight-dashboard-arcconfiguration-arcangle)" : {{Number}},
  "[ArcThickness](#cfn-quicksight-dashboard-arcconfiguration-arcthickness)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-arcconfiguration-syntax.yaml"></a>

```
  [ArcAngle](#cfn-quicksight-dashboard-arcconfiguration-arcangle): {{Number}}
  [ArcThickness](#cfn-quicksight-dashboard-arcconfiguration-arcthickness): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-arcconfiguration-properties"></a>

`ArcAngle`  <a name="cfn-quicksight-dashboard-arcconfiguration-arcangle"></a>
The option that determines the arc angle of a `GaugeChartVisual`.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ArcThickness`  <a name="cfn-quicksight-dashboard-arcconfiguration-arcthickness"></a>
The options that determine the arc thickness of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Allowed values*: `SMALL | MEDIUM | LARGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
