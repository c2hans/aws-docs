---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-radarchartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard RadarChartSortConfiguration
<a name="aws-properties-quicksight-dashboard-radarchartsortconfiguration"></a>

The sort configuration of a `RadarChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-radarchartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-radarchartsortconfiguration-syntax.json"></a>

```
{
  "[CategoryItemsLimit](#cfn-quicksight-dashboard-radarchartsortconfiguration-categoryitemslimit)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-dashboard-radarchartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}},
  "[ColorItemsLimit](#cfn-quicksight-dashboard-radarchartsortconfiguration-coloritemslimit)" : {{ItemsLimitConfiguration}},
  "[ColorSort](#cfn-quicksight-dashboard-radarchartsortconfiguration-colorsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-radarchartsortconfiguration-syntax.yaml"></a>

```
  [CategoryItemsLimit](#cfn-quicksight-dashboard-radarchartsortconfiguration-categoryitemslimit): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-dashboard-radarchartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
  [ColorItemsLimit](#cfn-quicksight-dashboard-radarchartsortconfiguration-coloritemslimit): {{
    ItemsLimitConfiguration}}
  [ColorSort](#cfn-quicksight-dashboard-radarchartsortconfiguration-colorsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-radarchartsortconfiguration-properties"></a>

`CategoryItemsLimit`  <a name="cfn-quicksight-dashboard-radarchartsortconfiguration-categoryitemslimit"></a>
The category items limit for a radar chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-dashboard-radarchartsortconfiguration-categorysort"></a>
The category sort options of a radar chart.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorItemsLimit`  <a name="cfn-quicksight-dashboard-radarchartsortconfiguration-coloritemslimit"></a>
The color items limit of a radar chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorSort`  <a name="cfn-quicksight-dashboard-radarchartsortconfiguration-colorsort"></a>
The color sort configuration of a radar chart.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
