---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-linechartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LineChartSortConfiguration
<a name="aws-properties-quicksight-analysis-linechartsortconfiguration"></a>

The sort configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-analysis-linechartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-linechartsortconfiguration-syntax.json"></a>

```
{
  "[CategoryItemsLimitConfiguration](#cfn-quicksight-analysis-linechartsortconfiguration-categoryitemslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-analysis-linechartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}},
  "[ColorItemsLimitConfiguration](#cfn-quicksight-analysis-linechartsortconfiguration-coloritemslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[SmallMultiplesLimitConfiguration](#cfn-quicksight-analysis-linechartsortconfiguration-smallmultipleslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[SmallMultiplesSort](#cfn-quicksight-analysis-linechartsortconfiguration-smallmultiplessort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-linechartsortconfiguration-syntax.yaml"></a>

```
  [CategoryItemsLimitConfiguration](#cfn-quicksight-analysis-linechartsortconfiguration-categoryitemslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-analysis-linechartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
  [ColorItemsLimitConfiguration](#cfn-quicksight-analysis-linechartsortconfiguration-coloritemslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [SmallMultiplesLimitConfiguration](#cfn-quicksight-analysis-linechartsortconfiguration-smallmultipleslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [SmallMultiplesSort](#cfn-quicksight-analysis-linechartsortconfiguration-smallmultiplessort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-linechartsortconfiguration-properties"></a>

`CategoryItemsLimitConfiguration`  <a name="cfn-quicksight-analysis-linechartsortconfiguration-categoryitemslimitconfiguration"></a>
The limit on the number of categories that are displayed in a line chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-analysis-linechartsortconfiguration-categorysort"></a>
The sort configuration of the category fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorItemsLimitConfiguration`  <a name="cfn-quicksight-analysis-linechartsortconfiguration-coloritemslimitconfiguration"></a>
The limit on the number of lines that are displayed in a line chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiplesLimitConfiguration`  <a name="cfn-quicksight-analysis-linechartsortconfiguration-smallmultipleslimitconfiguration"></a>
The limit on the number of small multiples panels that are displayed.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiplesSort`  <a name="cfn-quicksight-analysis-linechartsortconfiguration-smallmultiplessort"></a>
The sort configuration of the small multiples field.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
