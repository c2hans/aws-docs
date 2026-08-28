---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pluginvisualconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PluginVisualConfiguration
<a name="aws-properties-quicksight-analysis-pluginvisualconfiguration"></a>

The plugin visual configuration. This includes the field wells, sorting options, and persisted options of the plugin visual.

## Syntax
<a name="aws-properties-quicksight-analysis-pluginvisualconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pluginvisualconfiguration-syntax.json"></a>

```
{
  "[FieldWells](#cfn-quicksight-analysis-pluginvisualconfiguration-fieldwells)" : {{[ PluginVisualFieldWell, ... ]}},
  "[SortConfiguration](#cfn-quicksight-analysis-pluginvisualconfiguration-sortconfiguration)" : {{PluginVisualSortConfiguration}},
  "[VisualOptions](#cfn-quicksight-analysis-pluginvisualconfiguration-visualoptions)" : {{PluginVisualOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pluginvisualconfiguration-syntax.yaml"></a>

```
  [FieldWells](#cfn-quicksight-analysis-pluginvisualconfiguration-fieldwells): {{
    - PluginVisualFieldWell}}
  [SortConfiguration](#cfn-quicksight-analysis-pluginvisualconfiguration-sortconfiguration): {{
    PluginVisualSortConfiguration}}
  [VisualOptions](#cfn-quicksight-analysis-pluginvisualconfiguration-visualoptions): {{
    PluginVisualOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pluginvisualconfiguration-properties"></a>

`FieldWells`  <a name="cfn-quicksight-analysis-pluginvisualconfiguration-fieldwells"></a>
The field wells configuration of the plugin visual.
*Required*: No
*Type*: Array of [PluginVisualFieldWell](aws-properties-quicksight-analysis-pluginvisualfieldwell.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-pluginvisualconfiguration-sortconfiguration"></a>
The sort configuration of the plugin visual.
*Required*: No
*Type*: [PluginVisualSortConfiguration](aws-properties-quicksight-analysis-pluginvisualsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualOptions`  <a name="cfn-quicksight-analysis-pluginvisualconfiguration-visualoptions"></a>
The persisted properties of the plugin visual.
*Required*: No
*Type*: [PluginVisualOptions](aws-properties-quicksight-analysis-pluginvisualoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
