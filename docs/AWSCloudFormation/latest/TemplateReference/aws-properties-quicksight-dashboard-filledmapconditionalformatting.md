---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-filledmapconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FilledMapConditionalFormatting
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformatting"></a>

The conditional formatting of a `FilledMapVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformatting-syntax.json"></a>

```
{
  "[ConditionalFormattingOptions](#cfn-quicksight-dashboard-filledmapconditionalformatting-conditionalformattingoptions)" : {{[ FilledMapConditionalFormattingOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformatting-syntax.yaml"></a>

```
  [ConditionalFormattingOptions](#cfn-quicksight-dashboard-filledmapconditionalformatting-conditionalformattingoptions): {{
    - FilledMapConditionalFormattingOption}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformatting-properties"></a>

`ConditionalFormattingOptions`  <a name="cfn-quicksight-dashboard-filledmapconditionalformatting-conditionalformattingoptions"></a>
Conditional formatting options of a `FilledMapVisual`.
*Required*: Yes
*Type*: Array of [FilledMapConditionalFormattingOption](aws-properties-quicksight-dashboard-filledmapconditionalformattingoption.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
