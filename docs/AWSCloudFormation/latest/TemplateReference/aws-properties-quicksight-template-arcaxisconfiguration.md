---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-arcaxisconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ArcAxisConfiguration
<a name="aws-properties-quicksight-template-arcaxisconfiguration"></a>

The arc axis configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-arcaxisconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-arcaxisconfiguration-syntax.json"></a>

```
{
  "[Range](#cfn-quicksight-template-arcaxisconfiguration-range)" : {{ArcAxisDisplayRange}},
  "[ReserveRange](#cfn-quicksight-template-arcaxisconfiguration-reserverange)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-arcaxisconfiguration-syntax.yaml"></a>

```
  [Range](#cfn-quicksight-template-arcaxisconfiguration-range): {{
    ArcAxisDisplayRange}}
  [ReserveRange](#cfn-quicksight-template-arcaxisconfiguration-reserverange): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-arcaxisconfiguration-properties"></a>

`Range`  <a name="cfn-quicksight-template-arcaxisconfiguration-range"></a>
The arc axis range of a `GaugeChartVisual`.
*Required*: No
*Type*: [ArcAxisDisplayRange](aws-properties-quicksight-template-arcaxisdisplayrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReserveRange`  <a name="cfn-quicksight-template-arcaxisconfiguration-reserverange"></a>
The reserved range of the arc axis.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
