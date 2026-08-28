---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-linechartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard LineChartSortConfiguration
<a name="aws-properties-quicksight-dashboard-linechartsortconfiguration"></a>

The sort configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-dashboard-linechartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-linechartsortconfiguration-syntax.json"></a>

```
{
  "[CategoryItemsLimitConfiguration](#cfn-quicksight-dashboard-linechartsortconfiguration-categoryitemslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-dashboard-linechartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}},
  "[ColorItemsLimitConfiguration](#cfn-quicksight-dashboard-linechartsortconfiguration-coloritemslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[SmallMultiplesLimitConfiguration](#cfn-quicksight-dashboard-linechartsortconfiguration-smallmultipleslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[SmallMultiplesSort](#cfn-quicksight-dashboard-linechartsortconfiguration-smallmultiplessort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-linechartsortconfiguration-syntax.yaml"></a>

```
  [CategoryItemsLimitConfiguration](#cfn-quicksight-dashboard-linechartsortconfiguration-categoryitemslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-dashboard-linechartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
  [ColorItemsLimitConfiguration](#cfn-quicksight-dashboard-linechartsortconfiguration-coloritemslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [SmallMultiplesLimitConfiguration](#cfn-quicksight-dashboard-linechartsortconfiguration-smallmultipleslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [SmallMultiplesSort](#cfn-quicksight-dashboard-linechartsortconfiguration-smallmultiplessort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-linechartsortconfiguration-properties"></a>

`CategoryItemsLimitConfiguration`  <a name="cfn-quicksight-dashboard-linechartsortconfiguration-categoryitemslimitconfiguration"></a>
The limit on the number of categories that are displayed in a line chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-dashboard-linechartsortconfiguration-categorysort"></a>
The sort configuration of the category fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorItemsLimitConfiguration`  <a name="cfn-quicksight-dashboard-linechartsortconfiguration-coloritemslimitconfiguration"></a>
The limit on the number of lines that are displayed in a line chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiplesLimitConfiguration`  <a name="cfn-quicksight-dashboard-linechartsortconfiguration-smallmultipleslimitconfiguration"></a>
The limit on the number of small multiples panels that are displayed.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiplesSort`  <a name="cfn-quicksight-dashboard-linechartsortconfiguration-smallmultiplessort"></a>
The sort configuration of the small multiples field.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
