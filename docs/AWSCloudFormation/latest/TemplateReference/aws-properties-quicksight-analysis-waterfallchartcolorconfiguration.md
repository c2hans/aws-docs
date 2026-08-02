---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-waterfallchartcolorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis WaterfallChartColorConfiguration
<a name="aws-properties-quicksight-analysis-waterfallchartcolorconfiguration"></a>

The color configuration of a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-analysis-waterfallchartcolorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-waterfallchartcolorconfiguration-syntax.json"></a>

```
{
  "[GroupColorConfiguration](#cfn-quicksight-analysis-waterfallchartcolorconfiguration-groupcolorconfiguration)" : {{WaterfallChartGroupColorConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-waterfallchartcolorconfiguration-syntax.yaml"></a>

```
  [GroupColorConfiguration](#cfn-quicksight-analysis-waterfallchartcolorconfiguration-groupcolorconfiguration): {{
    WaterfallChartGroupColorConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-waterfallchartcolorconfiguration-properties"></a>

`GroupColorConfiguration`  <a name="cfn-quicksight-analysis-waterfallchartcolorconfiguration-groupcolorconfiguration"></a>
The color configuration for individual groups within a waterfall visual.
*Required*: No
*Type*: [WaterfallChartGroupColorConfiguration](aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
