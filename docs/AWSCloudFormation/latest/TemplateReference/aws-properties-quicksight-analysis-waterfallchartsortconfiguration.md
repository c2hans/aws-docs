---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-waterfallchartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis WaterfallChartSortConfiguration
<a name="aws-properties-quicksight-analysis-waterfallchartsortconfiguration"></a>

The sort configuration of a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-analysis-waterfallchartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-waterfallchartsortconfiguration-syntax.json"></a>

```
{
  "[BreakdownItemsLimit](#cfn-quicksight-analysis-waterfallchartsortconfiguration-breakdownitemslimit)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-analysis-waterfallchartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-waterfallchartsortconfiguration-syntax.yaml"></a>

```
  [BreakdownItemsLimit](#cfn-quicksight-analysis-waterfallchartsortconfiguration-breakdownitemslimit): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-analysis-waterfallchartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-waterfallchartsortconfiguration-properties"></a>

`BreakdownItemsLimit`  <a name="cfn-quicksight-analysis-waterfallchartsortconfiguration-breakdownitemslimit"></a>
The limit on the number of bar groups that are displayed.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-analysis-waterfallchartsortconfiguration-categorysort"></a>
The sort configuration of the category fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
