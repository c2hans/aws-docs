---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pluginvisualtablequerysort.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PluginVisualTableQuerySort
<a name="aws-properties-quicksight-analysis-pluginvisualtablequerysort"></a>

The table query sorting options for the plugin visual.

## Syntax
<a name="aws-properties-quicksight-analysis-pluginvisualtablequerysort-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pluginvisualtablequerysort-syntax.json"></a>

```
{
  "[ItemsLimitConfiguration](#cfn-quicksight-analysis-pluginvisualtablequerysort-itemslimitconfiguration)" : {{PluginVisualItemsLimitConfiguration}},
  "[RowSort](#cfn-quicksight-analysis-pluginvisualtablequerysort-rowsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pluginvisualtablequerysort-syntax.yaml"></a>

```
  [ItemsLimitConfiguration](#cfn-quicksight-analysis-pluginvisualtablequerysort-itemslimitconfiguration): {{
    PluginVisualItemsLimitConfiguration}}
  [RowSort](#cfn-quicksight-analysis-pluginvisualtablequerysort-rowsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pluginvisualtablequerysort-properties"></a>

`ItemsLimitConfiguration`  <a name="cfn-quicksight-analysis-pluginvisualtablequerysort-itemslimitconfiguration"></a>
The maximum amount of data to be returned by a query.
*Required*: No
*Type*: [PluginVisualItemsLimitConfiguration](aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowSort`  <a name="cfn-quicksight-analysis-pluginvisualtablequerysort-rowsort"></a>
Determines how data is sorted in the response.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
