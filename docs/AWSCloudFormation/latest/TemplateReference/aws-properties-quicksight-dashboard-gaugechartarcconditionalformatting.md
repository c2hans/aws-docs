---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-gaugechartarcconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GaugeChartArcConditionalFormatting
<a name="aws-properties-quicksight-dashboard-gaugechartarcconditionalformatting"></a>

The options that determine the presentation of the arc of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-gaugechartarcconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-gaugechartarcconditionalformatting-syntax.json"></a>

```
{
  "[ForegroundColor](#cfn-quicksight-dashboard-gaugechartarcconditionalformatting-foregroundcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-gaugechartarcconditionalformatting-syntax.yaml"></a>

```
  [ForegroundColor](#cfn-quicksight-dashboard-gaugechartarcconditionalformatting-foregroundcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-gaugechartarcconditionalformatting-properties"></a>

`ForegroundColor`  <a name="cfn-quicksight-dashboard-gaugechartarcconditionalformatting-foregroundcolor"></a>
The conditional formatting of the arc foreground color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
