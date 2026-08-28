---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetImageTooltipConfiguration
<a name="aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration"></a>

The tooltip configuration for a sheet image.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration-syntax.json"></a>

```
{
  "[TooltipText](#cfn-quicksight-dashboard-sheetimagetooltipconfiguration-tooltiptext)" : {{SheetImageTooltipText}},
  "[Visibility](#cfn-quicksight-dashboard-sheetimagetooltipconfiguration-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration-syntax.yaml"></a>

```
  [TooltipText](#cfn-quicksight-dashboard-sheetimagetooltipconfiguration-tooltiptext): {{
    SheetImageTooltipText}}
  [Visibility](#cfn-quicksight-dashboard-sheetimagetooltipconfiguration-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration-properties"></a>

`TooltipText`  <a name="cfn-quicksight-dashboard-sheetimagetooltipconfiguration-tooltiptext"></a>
The text that appears in the tooltip.
*Required*: No
*Type*: [SheetImageTooltipText](aws-properties-quicksight-dashboard-sheetimagetooltiptext.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-sheetimagetooltipconfiguration-visibility"></a>
The visibility of the tooltip.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
