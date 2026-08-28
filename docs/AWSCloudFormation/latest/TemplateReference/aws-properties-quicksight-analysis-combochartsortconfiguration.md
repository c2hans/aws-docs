---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-combochartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ComboChartSortConfiguration
<a name="aws-properties-quicksight-analysis-combochartsortconfiguration"></a>

The sort configuration of a `ComboChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-combochartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-combochartsortconfiguration-syntax.json"></a>

```
{
  "[CategoryItemsLimit](#cfn-quicksight-analysis-combochartsortconfiguration-categoryitemslimit)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-analysis-combochartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}},
  "[ColorItemsLimit](#cfn-quicksight-analysis-combochartsortconfiguration-coloritemslimit)" : {{ItemsLimitConfiguration}},
  "[ColorSort](#cfn-quicksight-analysis-combochartsortconfiguration-colorsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-combochartsortconfiguration-syntax.yaml"></a>

```
  [CategoryItemsLimit](#cfn-quicksight-analysis-combochartsortconfiguration-categoryitemslimit): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-analysis-combochartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
  [ColorItemsLimit](#cfn-quicksight-analysis-combochartsortconfiguration-coloritemslimit): {{
    ItemsLimitConfiguration}}
  [ColorSort](#cfn-quicksight-analysis-combochartsortconfiguration-colorsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-combochartsortconfiguration-properties"></a>

`CategoryItemsLimit`  <a name="cfn-quicksight-analysis-combochartsortconfiguration-categoryitemslimit"></a>
The item limit configuration for the category field well of a combo chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-analysis-combochartsortconfiguration-categorysort"></a>
The sort configuration of the category field well in a combo chart.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorItemsLimit`  <a name="cfn-quicksight-analysis-combochartsortconfiguration-coloritemslimit"></a>
The item limit configuration of the color field well in a combo chart.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorSort`  <a name="cfn-quicksight-analysis-combochartsortconfiguration-colorsort"></a>
The sort configuration of the color field well in a combo chart.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
