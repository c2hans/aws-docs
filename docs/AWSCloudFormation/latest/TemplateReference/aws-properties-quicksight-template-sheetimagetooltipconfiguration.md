---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sheetimagetooltipconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SheetImageTooltipConfiguration
<a name="aws-properties-quicksight-template-sheetimagetooltipconfiguration"></a>

The tooltip configuration for a sheet image.

## Syntax
<a name="aws-properties-quicksight-template-sheetimagetooltipconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sheetimagetooltipconfiguration-syntax.json"></a>

```
{
  "[TooltipText](#cfn-quicksight-template-sheetimagetooltipconfiguration-tooltiptext)" : {{SheetImageTooltipText}},
  "[Visibility](#cfn-quicksight-template-sheetimagetooltipconfiguration-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sheetimagetooltipconfiguration-syntax.yaml"></a>

```
  [TooltipText](#cfn-quicksight-template-sheetimagetooltipconfiguration-tooltiptext): {{
    SheetImageTooltipText}}
  [Visibility](#cfn-quicksight-template-sheetimagetooltipconfiguration-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-sheetimagetooltipconfiguration-properties"></a>

`TooltipText`  <a name="cfn-quicksight-template-sheetimagetooltipconfiguration-tooltiptext"></a>
The text that appears in the tooltip.
*Required*: No
*Type*: [SheetImageTooltipText](aws-properties-quicksight-template-sheetimagetooltiptext.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-sheetimagetooltipconfiguration-visibility"></a>
The visibility of the tooltip.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
