---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tableconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableConditionalFormatting
<a name="aws-properties-quicksight-template-tableconditionalformatting"></a>

The conditional formatting for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-template-tableconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tableconditionalformatting-syntax.json"></a>

```
{
  "[ConditionalFormattingOptions](#cfn-quicksight-template-tableconditionalformatting-conditionalformattingoptions)" : {{[ TableConditionalFormattingOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tableconditionalformatting-syntax.yaml"></a>

```
  [ConditionalFormattingOptions](#cfn-quicksight-template-tableconditionalformatting-conditionalformattingoptions): {{
    - TableConditionalFormattingOption}}
```

## Properties
<a name="aws-properties-quicksight-template-tableconditionalformatting-properties"></a>

`ConditionalFormattingOptions`  <a name="cfn-quicksight-template-tableconditionalformatting-conditionalformattingoptions"></a>
Conditional formatting options for a `PivotTableVisual`.
*Required*: No
*Type*: Array of [TableConditionalFormattingOption](aws-properties-quicksight-template-tableconditionalformattingoption.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
