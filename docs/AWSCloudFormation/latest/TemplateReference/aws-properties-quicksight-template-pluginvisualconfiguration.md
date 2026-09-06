---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pluginvisualconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PluginVisualConfiguration
<a name="aws-properties-quicksight-template-pluginvisualconfiguration"></a>

The plugin visual configuration. This includes the field wells, sorting options, and persisted options of the plugin visual.

## Syntax
<a name="aws-properties-quicksight-template-pluginvisualconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pluginvisualconfiguration-syntax.json"></a>

```
{
  "[FieldWells](#cfn-quicksight-template-pluginvisualconfiguration-fieldwells)" : {{[ PluginVisualFieldWell, ... ]}},
  "[SortConfiguration](#cfn-quicksight-template-pluginvisualconfiguration-sortconfiguration)" : {{PluginVisualSortConfiguration}},
  "[VisualOptions](#cfn-quicksight-template-pluginvisualconfiguration-visualoptions)" : {{PluginVisualOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pluginvisualconfiguration-syntax.yaml"></a>

```
  [FieldWells](#cfn-quicksight-template-pluginvisualconfiguration-fieldwells): {{
    - PluginVisualFieldWell}}
  [SortConfiguration](#cfn-quicksight-template-pluginvisualconfiguration-sortconfiguration): {{
    PluginVisualSortConfiguration}}
  [VisualOptions](#cfn-quicksight-template-pluginvisualconfiguration-visualoptions): {{
    PluginVisualOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-pluginvisualconfiguration-properties"></a>

`FieldWells`  <a name="cfn-quicksight-template-pluginvisualconfiguration-fieldwells"></a>
The field wells configuration of the plugin visual.
*Required*: No
*Type*: Array of [PluginVisualFieldWell](aws-properties-quicksight-template-pluginvisualfieldwell.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-template-pluginvisualconfiguration-sortconfiguration"></a>
The sort configuration of the plugin visual.
*Required*: No
*Type*: [PluginVisualSortConfiguration](aws-properties-quicksight-template-pluginvisualsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualOptions`  <a name="cfn-quicksight-template-pluginvisualconfiguration-visualoptions"></a>
The persisted properties of the plugin visual.
*Required*: No
*Type*: [PluginVisualOptions](aws-properties-quicksight-template-pluginvisualoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
