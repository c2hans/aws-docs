---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-combochartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ComboChartSortConfiguration
<a name="aws-properties-quicksight-dashboard-combochartsortconfiguration"></a>

The sort configuration of a `ComboChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-combochartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-combochartsortconfiguration-syntax.json"></a>

```
{
  "[CategoryItemsLimit](#cfn-quicksight-dashboard-combochartsortconfiguration-categoryitemslimit)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-dashboard-combochartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}},
  "[ColorItemsLimit](#cfn-quicksight-dashboard-combochartsortconfiguration-coloritemslimit)" : {{ItemsLimitConfiguration}},
  "[ColorSort](#cfn-quicksight-dashboard-combochartsortconfiguration-colorsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-combochartsortconfiguration-syntax.yaml"></a>

```
  [CategoryItemsLimit](#cfn-quicksight-dashboard-combochartsortconfiguration-categoryitemslimit): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-dashboard-combochartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
  [ColorItemsLimit](#cfn-quicksight-dashboard-combochartsortconfiguration-coloritemslimit): {{
    ItemsLimitConfiguration}}
  [ColorSort](#cfn-quicksight-dashboard-combochartsortconfiguration-colorsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-combochartsortconfiguration-properties"></a>

`CategoryItemsLimit`  <a name="cfn-quicksight-dashboard-combochartsortconfiguration-categoryitemslimit"></a>
The item limit configuration for the category field well of a combo chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-dashboard-combochartsortconfiguration-categorysort"></a>
The sort configuration of the category field well in a combo chart.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorItemsLimit`  <a name="cfn-quicksight-dashboard-combochartsortconfiguration-coloritemslimit"></a>
The item limit configuration of the color field well in a combo chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorSort`  <a name="cfn-quicksight-dashboard-combochartsortconfiguration-colorsort"></a>
The sort configuration of the color field well in a combo chart.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
