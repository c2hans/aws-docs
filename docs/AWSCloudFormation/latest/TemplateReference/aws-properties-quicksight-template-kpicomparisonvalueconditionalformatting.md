---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPIComparisonValueConditionalFormatting
<a name="aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting"></a>

The conditional formatting for the comparison value of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting-syntax.json"></a>

```
{
  "[Icon](#cfn-quicksight-template-kpicomparisonvalueconditionalformatting-icon)" : {{ConditionalFormattingIcon}},
  "[TextColor](#cfn-quicksight-template-kpicomparisonvalueconditionalformatting-textcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting-syntax.yaml"></a>

```
  [Icon](#cfn-quicksight-template-kpicomparisonvalueconditionalformatting-icon): {{
    ConditionalFormattingIcon}}
  [TextColor](#cfn-quicksight-template-kpicomparisonvalueconditionalformatting-textcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting-properties"></a>

`Icon`  <a name="cfn-quicksight-template-kpicomparisonvalueconditionalformatting-icon"></a>
The conditional formatting of the comparison value's icon.
*Required*: No
*Type*: [ConditionalFormattingIcon](aws-properties-quicksight-template-conditionalformattingicon.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-quicksight-template-kpicomparisonvalueconditionalformatting-textcolor"></a>
The conditional formatting of the comparison value's text color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-template-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
