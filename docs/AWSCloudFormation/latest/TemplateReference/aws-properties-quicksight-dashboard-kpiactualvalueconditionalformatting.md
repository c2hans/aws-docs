---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard KPIActualValueConditionalFormatting
<a name="aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting"></a>

The conditional formatting for the actual value of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting-syntax.json"></a>

```
{
  "[Icon](#cfn-quicksight-dashboard-kpiactualvalueconditionalformatting-icon)" : {{ConditionalFormattingIcon}},
  "[TextColor](#cfn-quicksight-dashboard-kpiactualvalueconditionalformatting-textcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting-syntax.yaml"></a>

```
  [Icon](#cfn-quicksight-dashboard-kpiactualvalueconditionalformatting-icon): {{
    ConditionalFormattingIcon}}
  [TextColor](#cfn-quicksight-dashboard-kpiactualvalueconditionalformatting-textcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting-properties"></a>

`Icon`  <a name="cfn-quicksight-dashboard-kpiactualvalueconditionalformatting-icon"></a>
The conditional formatting of the actual value's icon.
*Required*: No
*Type*: [ConditionalFormattingIcon](aws-properties-quicksight-dashboard-conditionalformattingicon.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-quicksight-dashboard-kpiactualvalueconditionalformatting-textcolor"></a>
The conditional formatting of the actual value's text color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
