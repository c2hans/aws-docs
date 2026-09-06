---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottableconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableConditionalFormatting
<a name="aws-properties-quicksight-template-pivottableconditionalformatting"></a>

The conditional formatting for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-template-pivottableconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottableconditionalformatting-syntax.json"></a>

```
{
  "[ConditionalFormattingOptions](#cfn-quicksight-template-pivottableconditionalformatting-conditionalformattingoptions)" : {{[ PivotTableConditionalFormattingOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottableconditionalformatting-syntax.yaml"></a>

```
  [ConditionalFormattingOptions](#cfn-quicksight-template-pivottableconditionalformatting-conditionalformattingoptions): {{
    - PivotTableConditionalFormattingOption}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottableconditionalformatting-properties"></a>

`ConditionalFormattingOptions`  <a name="cfn-quicksight-template-pivottableconditionalformatting-conditionalformattingoptions"></a>
Conditional formatting options for a `PivotTableVisual`.
*Required*: No
*Type*: Array of [PivotTableConditionalFormattingOption](aws-properties-quicksight-template-pivottableconditionalformattingoption.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
