---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-funnelchartsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FunnelChartSortConfiguration
<a name="aws-properties-quicksight-analysis-funnelchartsortconfiguration"></a>

The sort configuration of a `FunnelChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-funnelchartsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-funnelchartsortconfiguration-syntax.json"></a>

```
{
  "[CategoryItemsLimit](#cfn-quicksight-analysis-funnelchartsortconfiguration-categoryitemslimit)" : {{ItemsLimitConfiguration}},
  "[CategorySort](#cfn-quicksight-analysis-funnelchartsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-funnelchartsortconfiguration-syntax.yaml"></a>

```
  [CategoryItemsLimit](#cfn-quicksight-analysis-funnelchartsortconfiguration-categoryitemslimit): {{
    ItemsLimitConfiguration}}
  [CategorySort](#cfn-quicksight-analysis-funnelchartsortconfiguration-categorysort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-funnelchartsortconfiguration-properties"></a>

`CategoryItemsLimit`  <a name="cfn-quicksight-analysis-funnelchartsortconfiguration-categoryitemslimit"></a>
The limit on the number of categories displayed.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategorySort`  <a name="cfn-quicksight-analysis-funnelchartsortconfiguration-categorysort"></a>
The sort configuration of the category fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
