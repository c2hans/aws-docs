---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tableinlinevisualization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableInlineVisualization
<a name="aws-properties-quicksight-template-tableinlinevisualization"></a>

The inline visualization of a specific type to display within a chart.

## Syntax
<a name="aws-properties-quicksight-template-tableinlinevisualization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tableinlinevisualization-syntax.json"></a>

```
{
  "[DataBars](#cfn-quicksight-template-tableinlinevisualization-databars)" : {{DataBarsOptions}},
  "[Sparklines](#cfn-quicksight-template-tableinlinevisualization-sparklines)" : {{SparklinesOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tableinlinevisualization-syntax.yaml"></a>

```
  [DataBars](#cfn-quicksight-template-tableinlinevisualization-databars): {{
    DataBarsOptions}}
  [Sparklines](#cfn-quicksight-template-tableinlinevisualization-sparklines): {{
    SparklinesOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-tableinlinevisualization-properties"></a>

`DataBars`  <a name="cfn-quicksight-template-tableinlinevisualization-databars"></a>
The configuration of the inline visualization of the data bars within a chart.
*Required*: No
*Type*: [DataBarsOptions](aws-properties-quicksight-template-databarsoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sparklines`  <a name="cfn-quicksight-template-tableinlinevisualization-sparklines"></a>
The configuration of the inline visualization of the sparklines within a chart.
*Required*: No
*Type*: [SparklinesOptions](aws-properties-quicksight-template-sparklinesoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
